import sys
import objc
import reverse_geocoder
from CoreLocation import CLLocationManager, kCLLocationAccuracyBest
from Foundation import NSRunLoop, NSDate


# ── Localisation GPS ─────────────────────────────────────────────────────────

class LocationDelegate(objc.lookUpClass("NSObject")):
    def init(self):
        self = objc.super(LocationDelegate, self).init()
        if self:
            self.location = None
            self.error    = None
            self.is_done  = False
        return self

    def locationManager_didUpdateLocations_(self, manager, locations):
        if locations:
            self.location = locations.lastObject()
            self.is_done  = True

    def locationManager_didFailWithError_(self, manager, error):
        self.error   = error.localizedDescription()
        self.is_done = True


def get_mac_location():
    with objc.autorelease_pool():
        manager  = CLLocationManager.alloc().init()
        delegate = LocationDelegate.alloc().init()
        manager.setDelegate_(delegate)
        manager.setDesiredAccuracy_(kCLLocationAccuracyBest)
        manager.startUpdatingLocation()

        print("Demande de localisation envoyée… En attente du système.")

        run_loop = NSRunLoop.currentRunLoop()
        while not delegate.is_done:
            run_loop.runMode_beforeDate_(
                "NSDefaultRunLoopMode",
                NSDate.dateWithTimeIntervalSinceNow_(0.1)
            )

        manager.stopUpdatingLocation()

        if delegate.error:
            print(f"Erreur GPS : {delegate.error}")
            return None

        return delegate.location


# ── Géocodage inverse offline (GeoNames embarqué) ────────────────────────────

def reverse_geocode_local(lat: float, lon: float) -> str:
    """
    Retourne 'Ville, Région, Pays' sans aucune connexion réseau.
    Utilise la base GeoNames bundlée dans le package reverse_geocoder.
    Précision : ville / département (pas la rue).
    """
    results = reverse_geocoder.search((lat, lon), verbose=False)
    if not results:
        return "Lieu inconnu"
    r = results[0]
    parts = [p for p in [r.get("name"), r.get("admin2"), r.get("admin1"), r.get("cc")] if p]
    return ", ".join(parts)


# ── Point d'entrée ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    if sys.platform != "darwin":
        print("Ce script ne fonctionne que sur macOS.")
        sys.exit(1)

    location = get_mac_location()
    if not location:
        sys.exit(1)

    coords = location.coordinate()
    lat    = coords.latitude
    lon    = coords.longitude

    print("\n--- Localisation du Mac ---")
    print(f"Latitude  : {lat}")
    print(f"Longitude : {lon}")
    print(f"Précision : {location.horizontalAccuracy()} mètres")
    print(f"Altitude  : {location.altitude()} mètres")

    place = reverse_geocode_local(lat, lon)
    print(f"\n📍 {place}")

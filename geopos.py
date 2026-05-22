import sys
import objc
from CoreLocation import (
    CLLocationManager,
    kCLLocationAccuracyBest,
    kCLAuthorizationStatusAuthorizedAlways,
    kCLAuthorizationStatusAuthorizedWhenInUse,
    kCLAuthorizationStatusDenied,
    kCLAuthorizationStatusRestricted,
    kCLAuthorizationStatusNotDetermined,
)
from Foundation import NSRunLoop, NSDate


class LocationDelegate(objc.lookUpClass("NSObject")):
    def init(self):
        self = objc.super(LocationDelegate, self).init()
        if self:
            self.location = None
            self.error = None
            self.is_done = False
        return self

    # Called on macOS 11+ when authorization status changes
    def locationManagerDidChangeAuthorization_(self, manager):
        self._handleAuthStatus(manager, manager.authorizationStatus())

    # Called on macOS < 11 when authorization status changes
    def locationManager_didChangeAuthorizationStatus_(self, manager, status):
        self._handleAuthStatus(manager, status)

    def _handleAuthStatus(self, manager, status):
        if status in (kCLAuthorizationStatusAuthorizedAlways,
                      kCLAuthorizationStatusAuthorizedWhenInUse):
            # Permission granted — now safe to start
            manager.startUpdatingLocation()
        elif status == kCLAuthorizationStatusDenied:
            self.error = (
                "Accès à la localisation refusé.\n"
                "→ Activez l'accès dans : Réglages système › Confidentialité & sécurité "
                "› Services de localisation › Terminal (ou votre terminal)."
            )
            self.is_done = True
        elif status == kCLAuthorizationStatusRestricted:
            self.error = "Accès à la localisation restreint par une politique système."
            self.is_done = True
        # kCLAuthorizationStatusNotDetermined : en attente de la réponse utilisateur, on ne fait rien

    def locationManager_didUpdateLocations_(self, manager, locations):
        if locations:
            self.location = locations.lastObject()
            self.is_done = True

    def locationManager_didFailWithError_(self, manager, error):
        self.error = error.localizedDescription()
        self.is_done = True


def get_mac_location():
    with objc.autorelease_pool():
        manager = CLLocationManager.alloc().init()
        delegate = LocationDelegate.alloc().init()
        manager.setDelegate_(delegate)
        manager.setDesiredAccuracy_(kCLLocationAccuracyBest)

        # Demande d'autorisation AVANT de lancer les mises à jour.
        # startUpdatingLocation() est appelé dans le delegate une fois l'autorisation accordée.
        status = manager.authorizationStatus()
        if status == kCLAuthorizationStatusNotDetermined:
            manager.requestWhenInUseAuthorization()
            print("Demande d'autorisation envoyée... En attente de la réponse.")
        elif status in (kCLAuthorizationStatusAuthorizedAlways,
                        kCLAuthorizationStatusAuthorizedWhenInUse):
            # Déjà autorisé : on démarre directement
            manager.startUpdatingLocation()
            print("Autorisation déjà accordée. Demande de localisation envoyée...")
        elif status == kCLAuthorizationStatusDenied:
            print(
                "Erreur : accès à la localisation refusé.\n"
                "→ Réglages système › Confidentialité & sécurité › Services de localisation "
                "› activez votre terminal."
            )
            return None
        elif status == kCLAuthorizationStatusRestricted:
            print("Erreur : accès à la localisation restreint par une politique système.")
            return None

        # Boucle d'événements macOS : attend le résultat asynchrone
        run_loop = NSRunLoop.currentRunLoop()
        while not delegate.is_done:
            run_loop.runMode_beforeDate_(
                "NSDefaultRunLoopMode",
                NSDate.dateWithTimeIntervalSinceNow_(0.1)
            )

        manager.stopUpdatingLocation()

        if delegate.error:
            print(f"Erreur : {delegate.error}")
            return None

        return delegate.location


if __name__ == "__main__":
    if sys.platform != "darwin":
        print("Ce script ne fonctionne que sur macOS.")
        sys.exit(1)

    location = get_mac_location()

    if location:
        coords = location.coordinate()
        print("\n--- Localisation du Mac ---")
        print(f"Latitude  : {coords.latitude}")
        print(f"Longitude : {coords.longitude}")
        print(f"Précision : {location.horizontalAccuracy()} mètres")
        print(f"Altitude  : {location.altitude()} mètres")

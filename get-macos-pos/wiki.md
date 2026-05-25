# Get macOS Position

**File:** [`Get-MacOS-Pos.py`](Get-MacOS-Pos.py)

Fetches your Mac's current GPS coordinates using CoreLocation (the same framework used by Maps and Find My), then reverse-geocodes them to a human-readable location — entirely offline using a bundled GeoNames database.

---

## Requirements

- **macOS only**
- Location Services must be enabled for Terminal (or your IDE) in **System Settings → Privacy & Security → Location Services**

```bash
pip install pyobjc-framework-CoreLocation reverse_geocoder
```

---

## Usage

```bash
python3 Get-MacOS-Pos.py
```

No arguments needed. The script prompts macOS for your location, waits for a fix, then prints the result.

---

## Example output

```
Location request sent… Waiting for system.

--- Mac Location ---
Latitude  : 48.8566
Longitude : 2.3522
Accuracy  : 65.0 meters
Altitude  : 35.2 meters

📍 Paris, Île-de-France, FR
```

---

## How it works

1. **CoreLocation** — Uses Apple's `CLLocationManager` via `pyobjc` to request a GPS/Wi-Fi/cell fix at best-available accuracy. The script runs a `NSRunLoop` tick loop (100 ms intervals) while it waits so the delegate callbacks can fire on the main thread.

2. **Reverse geocoding** — Once coordinates are obtained, [`reverse_geocoder`](https://github.com/thampiman/reverse-geocoder) looks them up against a local copy of the GeoNames dataset (packed into the library). No network call is made. It returns city, region/state, and country code.

---

## Notes

- **First run:** macOS will show a permission dialog asking whether to allow Terminal to access your location. You must click **Allow** or the script will exit with a GPS error.
- **Accuracy** depends on your hardware. A MacBook with Wi-Fi scanning usually achieves 20–100 m accuracy. A Mac mini or desktop with no GPS chip relies on IP geolocation as a fallback, which can be off by several kilometers.
- Reverse geocoding precision is at the **city / district level** — it won't tell you the street.

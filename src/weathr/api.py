import requests
from typing import Any

BASE_URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
HEADERS = {
    "User-Agent": "weathr (github.com/<username>)"
}

def fetchForecast(lat: float, lon: float) -> dict[str, Any]:
    url = f"{BASE_URL}?lat={lat}&lon={lon}"
    resp = requests.get(url, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.json()
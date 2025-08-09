from datetime import datetime
from typing import Any
from zoneinfo import ZoneInfo

def formatForecast(data: dict[str, Any], tz: str = "Europe/Oslo") -> list[dict[str, Any]]:
    tzinfo = ZoneInfo(tz)
    timeseries = data.get("properties", {}).get("timeseries", [])
    formatted = []

    for entry in timeseries:
        # Parse and convert the time
        timeUTC = datetime.fromisoformat(entry["time"].replace("Z", "+00:00"))
        localTime = timeUTC.astimezone(tzinfo)

        details = entry.get("data", {}).get("instant", {}).get("details", {})
        symbol = entry.get("data", {}).get("next_1_hours", {}).get("summary", {}).get("symbol_code")
        # "Precipitation" = just a fancy meteorology word for stuff falling from the sky
        precipitation = entry.get("data", {}).get("next_1_hours", {}).get("details", {}).get("precipitation_amount")

        formatted.append({
            "time": localTime.strftime("%Y-%m-%d %H:%M"),
            "temperature": details.get("air_temperature"),
            "symbol": symbol,
            "precipitation_mm": precipitation
        })

    return formatted
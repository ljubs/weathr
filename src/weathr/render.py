from rich.console import Console
from rich.table import Table

# Mapping yr.no symbol codes to emojis
SYMBOL_EMOJIS = {
    "clearsky_day": "☀️",
    "clearsky_night": "🌙",
    "partlycloudy_day": "⛅",
    "partlycloudy_night": "☁️",
    "cloudy": "☁️",
    "lightrain": "🌦️",
    "rain": "🌧️",
    "heavyrain": "🌧️",
    "snow": "❄️",
    "lightsnow": "🌨️",
    "fog": "🌫️",
}

def renderForecast(forecast: list[dict[str, any]]) -> None:
    console = Console()

    table = Table(title="Weather Forecast", show_lines=True)
    table.add_column("Time", justify="center", style="cyan")
    table.add_column("Temp (°C)", justify="center", style="magenta")
    table.add_column("Weather", justify="center")
    table.add_column("Precip (mm)", justify="center", style="blue")

    for entry in forecast:
        symbol = SYMBOL_EMOJIS.get(entry["symbol"], entry["symbol"] or "?")
        table.add_row(
            entry["time"],
            f"{entry['temperature']:.1f}" if entry["temperature"] is not None else "-",
            symbol,
            f"{entry['precipitation_mm']:.1f}" if entry["precipitation_mm"] is not None else "-"
        )

    console.print(table)
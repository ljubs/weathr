from api import fetchForecast
from cli import parseArgs
from formatter import formatForecast
from render import renderForecast

def main():
    # Parse CLI arguments
    args = parseArgs()
    # Fetch raw forecast data
    rawData = fetchForecast(args.lat, args.lon)
    # Format the data
    formatted = formatForecast(rawData)
    # Render the forecast in the terminal
    renderForecast(formatted)

if __name__ == "__main__":
    main()
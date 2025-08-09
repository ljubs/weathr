import argparse

def parseArgs():
    parser = argparse.ArgumentParser(
        description="A simple CLI tool to fetch and display weather data using a weather API.",
        usage="",
        epilog="Example: weathr --lat 59.91 --lon 10.75"
    )

    parser.add_argument(
        "--lat",
        type=float,
        required=True,
        help="Latitude of the location, e.g., 59.91"
    )

    parser.add_argument(
        "--lon",
        type=float,
        required=True,
        help="Longitude of the location, e.g., 10.75"
    )

    return parser.parse_args()
import requests
import math
from datetime import datetime
import time

# Constants for Seattle's geographical coordinates
SEATTLE_LAT = 47.6062
SEATTLE_LON = -122.3321

def get_iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.json()
    if data["message"] == "success":
        iss_position = data["iss_position"]
        iss_lat = float(iss_position["latitude"])
        iss_lon = float(iss_position["longitude"])
        return iss_lat, iss_lon
    else:
        raise Exception("Failed to fetch ISS location")

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of Earth in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c  # Distance in kilometers

def get_relative_position_to_seattle():
    iss_lat, iss_lon = get_iss_location()
    distance = calculate_distance(SEATTLE_LAT, SEATTLE_LON, iss_lat, iss_lon)
    direction = ""
    if iss_lat > SEATTLE_LAT:
        direction += "north"
    elif iss_lat < SEATTLE_LAT:
        direction += "south"
    if iss_lon > SEATTLE_LON:
        direction += "east"
    elif iss_lon < SEATTLE_LON:
        direction += "west"
    return distance, direction, (iss_lat, iss_lon)

def track_iss_position():
    while True:
        try:
            distance, direction, iss_coords = get_relative_position_to_seattle()
            print(f"[{datetime.now()}] The ISS is currently located at {iss_coords} (latitude, longitude).")
            print(f"It is approximately {distance:.2f} km {direction} of Seattle.")
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(30)  # Wait for 30 seconds before the next query

if __name__ == "__main__":
    track_iss_position()
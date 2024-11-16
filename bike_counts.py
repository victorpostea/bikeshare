import requests

def fetch_station_info():
    """
    Fetches station information from Bike Share Toronto's GBFS feed.
    Returns a dictionary mapping station names to station IDs.
    """
    url = "https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_information"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching station information.")
        return {}
    
    data = response.json()
    station_info = {}
    for station in data['data']['stations']:
        name = station['name']
        station_id = station['station_id']
        station_info[name] = station_id
    
    return station_info

def fetch_bike_counts():
    """
    Fetches real-time bike counts from Bike Share Toronto's GBFS feed.
    Returns a dictionary mapping station IDs to bike counts.
    """
    url = "https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_status"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching bike counts.")
        return {}
    
    data = response.json()
    bike_counts = {}
    for station in data['data']['stations']:
        station_id = station['station_id']
        num_bikes = station['num_bikes_available']
        bike_counts[station_id] = num_bikes
    
    return bike_counts

def check_for_rebalancing(stations_info):
    """
    Checks the bike counts and prints a message if rebalancing is needed.
    """
    for station_info in stations_info:
        station = station_info['name']
        bike_count = station_info['bike_count']
        if bike_count < 7 or bike_count > 15:
            print(f"Rebalance needed at station: {station} (Bike count: {bike_count})")

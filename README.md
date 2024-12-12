# Bikeshare Clustering and Rebalancing Backend

This repository contains the backend code for a bikeshare system that focuses on clustering stations and determining rebalancing needs using Neo4j and API integrations. This backend is a foundational component of an eventual full-stack application that incorporates quantum algorithms for optimization.

## Features

- **Clustering Stations**: Identify clusters of bikeshare stations based on proximity using the Haversine formula and a geolocation API.
- **Dynamic Bike Counts**: Fetch real-time bike counts for stations and determine rebalancing needs based on preset thresholds.
- **Neo4j Integration**: Store clusters and distances between stations as graph data in a Neo4j database.

## Project Structure

```
.
├── get_clusters
│   ├── calculate_clusters.py
│   ├── fetch_coordinates.py
│   ├── station_coordinates_cache.json
│   └── unique_station_names.txt
│
│── bike_counts.py
│── rebalance_log.txt
```

### `get_clusters` Directory

This directory handles station clustering and proximity calculations.

- **`calculate_clusters.py`**: 
  - Prompts for a center station and either a radius or the number of nearby stations to include in a cluster.
  - Uses the Haversine formula to calculate distances.
  - Fetches station coordinates from `station_coordinates_cache.json`.
  - Pings a geolocation API for missing coordinates and updates the cache.
  - Generates Neo4j queries to store clusters as nodes and edges with distances.

- **`fetch_coordinates.py`**:
  - A utility script for fetching and caching station coordinates using a geolocation API.

- **`station_coordinates_cache.json`**:
  - A JSON file caching station coordinates to reduce API calls.

- **`unique_station_names.txt`**:
  - A list of unique station names used for clustering.

### `bikeshare` Directory

This directory handles real-time bike count management and rebalancing logic.

- **`bike_counts.py`**:
  - Reads data from the Neo4j database.
  - Fetches live bike count data from the Toronto Bikeshare API.
  - Determines which stations require rebalancing based on a static floor and ceiling threshold.
  - Logs rebalancing recommendations to `rebalance_log.txt`.
  - Future plans: Send rebalancing data to a quantum algorithm for optimization.

- **`rebalance_log.txt`**:
  - Logs stations identified for rebalancing.

## Setup

### Prerequisites

- Python 3.8+
- Neo4j Database
- Geolocation API Key (or can use the cached stations)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/victorpostea/bikeshare.git
   cd bikeshare
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Neo4j database and geolocation API key.

4. Configure API keys and database connection settings in the respective scripts.

## Usage

### Cluster Creation

1. Navigate to the `get_clusters` directory:
   ```bash
   cd get_clusters
   ```

2. Run the `calculate_clusters.py` script:
   ```bash
   python calculate_clusters.py
   ```

3. Follow the prompts to:
   - Specify a center station.
   - Choose a radius or number of nearby stations for the cluster.

4. The script will calculate distances, fetch coordinates if necessary, and send cluster data to the Neo4j database.

### Dynamic Bike Counts

1. Navigate to the `bikeshare` directory:
   ```bash
   cd bikeshare
   ```

2. Run the `bike_counts.py` script:
   ```bash
   python bike_counts.py
   ```

3. The script will:
   - Fetch bike counts for each station.
   - Determine stations needing rebalancing.
   - Log the results in `rebalance_log.txt`.

## Future Enhancements

- **Integration with Quantum Algorithm**: Ping rebalancing data to the quantum optimization algorithm for improved decision-making.
- **Full-Stack Application**: Develop a frontend to visualize station clusters and rebalancing needs.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

Feel free to reach out for support or questions regarding this repository.

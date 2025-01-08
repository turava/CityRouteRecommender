# City Route Recommender

## Overview
City Route Recommender is a Python-based application that models a city's points of interest and their connections as a weighted graph. The primary purpose of this application is to suggest optimal routes between two locations based on various criteria like shortest distance or the fewest stops.

## Features
- **Add Points of Interest**: Add nodes (locations) to the city map.
- **Connect Points**: Define weighted connections (edges) between nodes to represent roads or paths.
- **Find Shortest Distance**: Use Dijkstra's algorithm to calculate the shortest path between two locations.
- **Find Fewest Stops**: Retrieve the path with the fewest intermediate points.
- **Delete Points**: Remove a location and its associated connections from the graph.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/turava/CityRouteRecommender
   ```
2. Navigate to the project directory:
   ```bash
   cd city-route-recommender
   ```
3. Ensure you have Python 3.7 or above installed.
```


### Example Workflow
1. Add points of interest to the city map:
   ```python
   city.add_point("A")
   city.add_point("B")
   ```
2. Connect points with distances:
   ```python
   city.connect_points("A", "B", 10)
   ```
3. Find the shortest route between two locations:
   ```python
   route, distance = city.shortest_route("A", "B")
   print("Shortest route:", route)
   print("Distance:", distance)
   ```
4. Find the route with the fewest stops:
   ```python
   route = city.route_with_fewest_stops("A", "B")
   print("Fewest stops route:", route)
   ```

## Classes
### `Node`
Represents a point of interest or intersection.
- **Attributes**:
  - `name`: Name of the location.
  - `connections`: Dictionary of connected nodes with weights.

### `CityGraph`
Represents the city map.
- **Methods**:
  - `add_point(name)`: Adds a new location to the graph.
  - `connect_points(name_a, name_b, distance)`: Creates a weighted edge between two nodes.
  - `shortest_route(origin, destination)`: Finds the shortest path using Dijkstra's algorithm.
  - `route_with_fewest_stops(origin, destination)`: Finds the path with the fewest stops.
  - `remove_point(name)`: Removes a node and all its connections.

## Example
Here's a complete example of creating a city map and finding routes:

```python
from city_graph import CityGraph

# Initialize graph
city = CityGraph()

# Add points
city.add_point("A")
city.add_point("B")
city.add_point("C")

# Connect points
city.connect_points("A", "B", 5)
city.connect_points("B", "C", 10)
city.connect_points("A", "C", 15)

# Find shortest route
route, distance = city.shortest_route("A", "C")
print("Shortest route:", route, "Distance:", distance)

# Find fewest stops
route = city.route_with_fewest_stops("A", "C")
print("Route with fewest stops:", route)
```

## Tests
Run the test suite to ensure functionality:
```bash
pytest
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy coding!

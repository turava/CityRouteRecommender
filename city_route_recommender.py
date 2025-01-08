class Node:
    def __init__(self, name):
        self.name = name
        self.connections = {}

    def add_connection(self, neighbor, distance):
        self.connections[neighbor] = distance


class CityGraph:
    def __init__(self):
        self.nodes = {}

    def add_point(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)

    def connect_points(self, name_a, name_b, distance):
        if name_a in self.nodes and name_b in self.nodes:
            self.nodes[name_a].add_connection(self.nodes[name_b], distance)
            self.nodes[name_b].add_connection(self.nodes[name_a], distance)

    def remove_point(self, name):
        if name in self.nodes:
            for neighbor in self.nodes[name].connections:
                neighbor.connections.pop(self.nodes[name], None)
            self.nodes.pop(name)

    def shortest_route(self, origin, destination):
        import heapq

        if origin not in self.nodes or destination not in self.nodes:
            return None, float('inf')

        distances = {node: float('inf') for node in self.nodes}
        previous_nodes = {node: None for node in self.nodes}
        distances[origin] = 0

        priority_queue = [(0, origin)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.nodes[current_node].connections.items():
                distance = current_distance + weight
                if distance < distances[neighbor.name]:
                    distances[neighbor.name] = distance
                    previous_nodes[neighbor.name] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor.name))

        path, current = [], destination
        while previous_nodes[current]:
            path.insert(0, current)
            current = previous_nodes[current]
        if path:
            path.insert(0, current)

        return path, distances[destination]

    def route_with_fewest_stops(self, origin, destination):
        from collections import deque

        if origin not in self.nodes or destination not in self.nodes:
            return []

        visited = set()
        queue = deque([(origin, [origin])])

        while queue:
            current, path = queue.popleft()

            if current == destination:
                return path

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.nodes[current].connections:
                if neighbor.name not in visited:
                    queue.append((neighbor.name, path + [neighbor.name]))

        return []

# Example usage
if __name__ == "__main__":
    city = CityGraph()

    # Adding points
    for point in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
        city.add_point(point)

    # Connecting points
    city.connect_points("A", "B", 4)
    city.connect_points("A", "C", 2)
    city.connect_points("B", "C", 5)
    city.connect_points("B", "D", 10)
    city.connect_points("C", "E", 3)
    city.connect_points("D", "E", 7)
    city.connect_points("E", "F", 1)
    city.connect_points("F", "G", 8)
    city.connect_points("G", "H", 6)
    city.connect_points("H", "I", 4)
    city.connect_points("I", "J", 9)

    # Shortest route
    route, distance = city.shortest_route("A", "J")
    print(f"Shortest route from A to J: {route}, Distance: {distance}")

    # Route with fewest stops
    route = city.route_with_fewest_stops("A", "J")
    print(f"Route with fewest stops from A to J: {route}")

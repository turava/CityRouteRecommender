import unittest
from city_route_recommender import CityGraph

class TestCityGraph(unittest.TestCase):

    def setUp(self):
        self.city = CityGraph()
        
        # Adding points
        for point in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
            self.city.add_point(point)

        # Connecting points
        self.city.connect_points("A", "B", 4)
        self.city.connect_points("A", "C", 2)
        self.city.connect_points("B", "C", 5)
        self.city.connect_points("B", "D", 10)
        self.city.connect_points("C", "E", 3)
        self.city.connect_points("D", "E", 7)
        self.city.connect_points("E", "F", 1)
        self.city.connect_points("F", "G", 8)
        self.city.connect_points("G", "H", 6)
        self.city.connect_points("H", "I", 4)
        self.city.connect_points("I", "J", 9)

    def test_shortest_route(self):
        route, distance = self.city.shortest_route("A", "J")
        self.assertEqual(route, ["A", "C", "E", "F", "G", "H", "I", "J"])
        self.assertEqual(distance, 33)

    def test_route_with_fewest_stops(self):
        route = self.city.route_with_fewest_stops("A", "J")
        self.assertEqual(route, ["A", "C", "E", "F", "G", "H", "I", "J"])

    def test_add_point(self):
        self.city.add_point("K")
        self.assertIn("K", self.city.nodes)

    def test_connect_points(self):
        self.city.connect_points("A", "D", 15)
        self.assertIn(self.city.nodes["D"], self.city.nodes["A"].connections)
        self.assertEqual(self.city.nodes["A"].connections[self.city.nodes["D"]], 15)

    def test_remove_point(self):
        self.city.remove_point("E")
        self.assertNotIn("E", self.city.nodes)
        for node in self.city.nodes.values():
            self.assertNotIn(self.city.nodes.get("E"), node.connections)

if __name__ == "__main__":
    unittest.main()

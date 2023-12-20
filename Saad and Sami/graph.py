from heapq import heappop, heappush
import pandas as pd
from itertools import permutations

class CityGraph:
    def __init__(self):
        self.graph = {}

    def add_city(self, city):
        if city not in self.graph:
            self.graph[city] = {}

    def add_connection(self, city1, city2, distance):
        if city1 in self.graph and city2 in self.graph:
            self.graph[city1][city2] = distance
            self.graph[city2][city1] = distance  # For an undirected connection

    def dijkstra(self, start_city):
        distances = {city: float('inf') for city in self.graph}
        distances[start_city] = 0
        paths = {city: [] for city in self.graph}
        visited = set()
        heap = [(0, start_city)]

        while heap:
            curr_distance, curr_city = heappop(heap)

            if curr_city in visited:
                continue

            visited.add(curr_city)

            for neighbor, weight in self.graph[curr_city].items():
                distance = curr_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    paths[neighbor] = paths[curr_city] + [curr_city]
                    heappush(heap, (distance, neighbor))

        return distances, paths
    def retGraph(self):
        return self.graph
    def get_subgraph(self, vertices):
        subgraph = CityGraph()

        for vertex in vertices:
            if vertex in self.graph:
                subgraph.add_city(vertex)
                for neighbor, distance in self.graph[vertex].items():
                    if neighbor in vertices:
                        subgraph.add_city(neighbor)
                        subgraph.add_connection(vertex, neighbor, distance)

        return subgraph
def shortest_path_to_visit_all2(city_graph, vertices):
    all_paths = permutations(vertices)
    shortest_path = None
    shortest_distance = float('inf')

    for path in all_paths:
        total_distance = 0
        for i in range(len(path) - 1):
            if path[i] in city_graph.retGraph() and path[i + 1] in city_graph.retGraph()[path[i]]:
                total_distance += city_graph.retGraph()[path[i]][path[i + 1]]
            else:
                total_distance = float('inf')
                break

        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_path = path

    return shortest_distance, shortest_path
def combine_paths(city_graph, paths):
    combined_path = []
    for i in range(len(paths) - 1):
        path_from, path_to = paths[i], paths[i + 1]
        _, subpath = FindShortestPath(city_graph, path_from, path_to)
        combined_path.extend(subpath[:-1])  # Avoid adding the last node of the subpath to prevent duplicates
    combined_path.append(paths[-1])  # Add the last vertex
    return combined_path

def shortest_path_to_visit_all(city_graph, vertices):
    all_paths = permutations(vertices)
    shortest_path = None
    shortest_distance = float('inf')

    for path in all_paths:
        total_distance = 0
        paths = list(path)
        for i in range(len(paths) - 1):
            distance, _ = FindShortestPath(city_graph, paths[i], paths[i + 1])
            total_distance += distance

        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_path = path

    combined_shortest_path = combine_paths(city_graph, shortest_path)
    return shortest_distance, combined_shortest_path
def roundTrip(city_graph, vertices):
    shortest_Distance1,shortest_path1=shortest_path_to_visit_all(city_graph, vertices)
    shortest_Distance2,shortest_path2=shortest_path_to_visit_all(city_graph, vertices)
    shortest_Distance1 += shortest_Distance2
    shortest_path1.extend(shortest_path2)
    return shortest_Distance1,shortest_path1
def FindShortestPath(city_graph,start_city,destination_city):
    shortest_distances, shortest_paths = city_graph.dijkstra(start_city)
    distance_to_dest=0.0
    path_to_dest=[]
    if destination_city in shortest_paths:
        distance_to_dest = shortest_distances[destination_city]
        path_to_dest = shortest_paths[destination_city] + [destination_city]
    if path_to_dest == None:
        return None
    return distance_to_dest,path_to_dest
g= CityGraph()
g.add_city("a")
g.add_city("b")
g.add_city("c")
g.add_city("d")
g.add_city("e")
g.add_connection("a","b",2)
g.add_connection("a","c",4)
g.add_connection("c","e",3)
g.add_connection("e","d",1)
g.add_connection("d","b",7)
g.add_connection("c","b",1)
list_of_vertices = ["a", "b", "c"]
print(roundTrip(g,list_of_vertices))
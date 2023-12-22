from heapq import heappop, heappush
from itertools import permutations
import matplotlib.pyplot as plt
from collections import deque
import networkx as nx
import pandas as pd

path = "Algos/point.csv"
# cities = ["UET", "Shahdara", "Ferozewala", "Badshahi Mosque", "Thoker Naiz Baig", "chung", "Maraka", "Valencia", "DHA", "Lidher", "Taij Garh", "Jallo", "Paragon City", "Garhi Shahu", "Allama Iqbal Town", "Johar Town", "TownShip", "Wapda Town", "Kahna"]

class vertex:
    def __init__(self, data):
        self.data = data
        self.adjacent = []
        self.visited = False

class edge:
    def __init__(self, source, destination, weight):
        self.weight = weight
        self.source = source
        self.destination = destination

class Graph:
    def __init__(self):
        self._vertices = []
        self._edges = []

    def add_vertex(self, data):
        previous = self.find_vertex(data)
        if not previous:
            self._vertices.append(vertex(data))

    def add_edge(self, source, destination, weight):
        s = self.find_vertex(source)
        d = self.find_vertex(destination)
        if s and d:
            temp = edge(s, d, weight)
            self._edges.append(temp)
            s.adjacent.append(d)
            d.adjacent.append(s)
            # print("Edge added.")
        else:
            print("Add valid vertices first.")

    def find_vertex(self, data):
        for vertex in self._vertices:
            if vertex.data == data:
                return vertex
        return None

    def dfs(self, start_vertex, target):  # Depth First Search uses stack to implement
        for vertex in self._vertices:
            vertex.visited = False
        stack = [start_vertex]  # add the first vertex to the stack
        while stack:
            current_vertex = stack.pop()
            if not current_vertex.visited:
                # print(current_vertex.data, end=" ")
                if current_vertex.data == target:
                    return True
                current_vertex.visited = True

                # Add unvisited neighbors to the stack
                for n in reversed(current_vertex.adjacent):
                    if not n.visited:
                        stack.append(n)
        return False

    def bfs(self, start_vertex, target):  # Breadth First Search uses queue to implement
        for vertex in self._vertices:
            vertex.visited = False
        queue = deque([start_vertex])

        while queue:
            current_vertex = queue.popleft()
            if not current_vertex.visited:
                if current_vertex.data == target:
                    return True
                current_vertex.visited = True

                # Add unvisited neighbors to the queue
                for i in current_vertex.adjacent:
                    if not i.visited:
                        queue.append(i)
        return False

    def visualize(self):
        G = nx.Graph()
        for e in self._edges:
            G.add_edge(e.source.data, e.destination.data, weight=e.weight)

        pos = nx.spring_layout(G)  # You can choose other layouts as well
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw(
            G,
            pos,
            with_labels=True,
            font_weight="bold",
            node_size=1500,
            node_color="skyblue",
            font_size=8,
            edge_color="gray",
            width=2,
            edge_cmap=plt.cm.Blues,
        )
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    def show(self):
        for vertex in self._vertices:
            print(vertex.data, end=": ")
            for i in vertex.adjacent:
                print(i.data, end=" ")
            print()

class CityGraph:
    def __init__(self):
        self.graph = {}

    def add_city(self, city):
        if city not in self.graph:
            self.graph[city] = {}

    def find_city(self, city):
        if city in self.graph:
            return True
        return False
    
    def add_connection(self, city1, city2, distance):
        if city1 in self.graph and city2 in self.graph:
            self.graph[city1][city2] = distance
            self.graph[city2][city1] = distance                # For an undirected connection
        else:
            print("Invalid Vertices Ended")

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

def add_edges(g):
    df = pd.read_csv(path)
    data = df.values.tolist()
    for i in data:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
    for i in data:
        g.add_edge(i[0], i[1], i[2])

def FindShortestPath(city_graph, start_city, destination_city):
    if start_city not in city_graph.graph or destination_city not in city_graph.graph:
        return None, []

    shortest_distances, shortest_paths = city_graph.dijkstra(start_city)
    distance_to_dest=0.0
    path_to_dest=[]
    if destination_city in shortest_paths:
        distance_to_dest = shortest_distances[destination_city]
        path_to_dest = shortest_paths[destination_city] + [destination_city]
    if path_to_dest == None:
        return None
    return distance_to_dest,path_to_dest

def loadGraph(g):
    data = pd.read_csv(path)
    data=data.values.tolist()
    
    for i in range(len(data)):
        g.add_city(data[i][0])
        g.add_city(data[i][1])
    
    for i in range(len(data)):
        try:
            g.add_connection(data[i][0], data[i][1], float(data[i][2]))
        except:
            continue    

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

def main():
    graphDisplay = Graph()
    GraphCalculate = CityGraph()
    add_edges(graphDisplay)
    loadGraph(GraphCalculate)
    # for i in graphDisplay._vertices:
    #     print(i.data, end=": ")
    # for i in GraphCalculate.graph:
    #     print(i)
    # print(FindShortestPath(GraphCalculate, "Jallo", "TownShip"))
    # graphDisplay.visualize()
    result = graphDisplay.bfs(graphDisplay.find_vertex("UET"), "Jallo")
    print(result)

if __name__ == "__main__":
    main()

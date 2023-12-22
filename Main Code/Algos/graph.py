from heapq import heappop, heappush
import pandas as pd
import matplotlib as plt
import networkx as nx
import csv

class CityGraph:
    def __init__(self):
        self.graph = {}

    def add_city(self, city):
        if city not in self.graph:
            self.graph[city] = {}

    def add_connection(self, city1, city2, distance):
        if city1 in self.graph and city2 in self.graph:
            self.graph[city1][city2] = distance
            self.graph[city2][city1] = distance                # For an undirected connection

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

def FindShortestPath(city_graph, start_city, destination_city):
    shortest_distances, shortest_paths = city_graph.dijkstra(start_city)
    distance_to_dest=0.0
    path_to_dest=[]
    if destination_city in shortest_paths:
        distance_to_dest = shortest_distances[destination_city]
        path_to_dest = shortest_paths[destination_city] + [destination_city]
    if path_to_dest == None:
        return None
    return distance_to_dest,path_to_dest

def loadGraph(path):
    data = pd.read_csv(path)
    data=data.values.tolist()
    city_graph = CityGraph()
    
    for i in range(len(data)):
        city_graph.add_city(data[i][0])
        city_graph.add_city(data[i][1])
    
    for i in range(len(data)):
        try:
            city_graph.add_connection(data[i][0], data[i][1],float( data[i][2]))
        except:
            continue    
    return  city_graph

if __name__ == "__main__":
    # city_graph = loadGraph("data.csv")
    # distance,path = FindShortestPath(city_graph, "Wandaville","North Amber")
    # print(distance)
    # print(path)
    # for i in city_graph.graph:
    #     print(i)
    # city_graph.visualize()
    g = CityGraph()
    g.add_city('a')
    g.add_city('b')
    g.add_city('c')
    g.add_city('d')
    g.add_city('e')
    g.add_connection('a', 'b', 2)
    g.add_connection('a', 'c', 4)
    g.add_connection('b', 'c', 1)
    g.add_connection('e', 'c', 3)
    g.add_connection('e', 'd', 1)
    g.add_connection('b', 'd', 7)
    # print(FindShortestPath(g, 'a', 'd'))
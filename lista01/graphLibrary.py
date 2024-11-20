import heapq as hp
import math
import queue
from tkinter.constants import CURRENT
class Graph:
    def __init__(self,graph: dict={}) -> None:
        self.graph = graph;
    def add_edge(self,node1,node2,cost):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = cost;
    def add_node(self,node):
        if node in self.graph:
            pass
        else:
            self.graph[node] = {};
    def shortest_distances(self, source_node:str):
        distance = {}
        distances = {node: (math.inf) for node in self.graph}
        distances[source_node] = 0.0;
        #visited nodes set for performance (check if a node is in set)
        visited_nodes = set()
        priority_queue = [(source_node,0.0)]
        hp.heapify(priority_queue)
        while priority_queue:
            current_node,current_distance = hp.heappop(priority_queue);
            if current_node in visited_nodes:
                continue
            visited_nodes.add(current_node)
            for neighbor,cost in self.graph[current_node].items():
                aux_dist = current_distance + cost
                if aux_dist < distances[neighbor]:
                    distances[neighbor] = aux_dist
                    hp.heappush(priority_queue,(neighbor,aux_dist))
        return distances;
    def return_predecessors(self,distances: dict):
        pred = {node: None for node in self.graph}
        for node,distance in distances.items():
            for neighbor,cost in self.graph[node].items():
                if distances[neighbor] == distance+cost:
                    pred[neighbor] = node
        return pred
    def set_graph(self,_graph: dict):
        self.graph = _graph
    def get_file_graph(self,file_path: str):
        #follow the graphExample.txt pattern :)
        #TODO
        file = open(file_path)
        count = 0;
        for line in file:
            if (line == ""):
                continue
            aux=line.split(" ")
            #print("Node {} to Node {} with cost {}".format(aux[0],aux[1],aux[2]))
            self.add_edge(aux[0],aux[1],float(aux[2]))
            self.add_edge(aux[1],aux[0],float(aux[2]))
        file.close()
    def short_path(self,source:str,target: str):
        #Path list
        path = []
        predecessors = self.return_predecessors(self.shortest_distances(source))
        current_node = target;
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]
        path.reverse()
        for x in path:
            print(x)
    def print_graph(self):
        for node,neighbor in self.graph.items():
            print ("{} : {}".format(node,neighbor))
    def print_distances(self,source:str):
        print("Shortest distances from node {}".format(source))
        ds = self.shortest_distances(source)
        for node,distance in ds.items():
            print ("{} : {}".format(node,distance))
    def returnChange(self,change,currency):
        toGiveBack = [0] * len(currency)
        for pos,money in enumerate(reversed(currency)):
            while money <= change:
                change = change - money
                toGiveBack[len(currency)-pos-1] += 1
        print(toGiveBack)
        return(toGiveBack)

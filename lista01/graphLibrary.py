import heapq as hp
class Graph:
    def __init__(self,_graph: dict={}):
        self.graph = _graph;
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
        distances = {node: float(-1.0) for node in self.graph}
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
        pred = {node: "" for node in self.graph}
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
        pass
    def uniform_cost_search(self,source:str,target: str):
        #Path list
        path = []
        predecessors = self.return_predecessors(self.shortest_distances(source))
        current_node = target;
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]
        path.reverse()
        return path;

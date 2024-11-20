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
        self.graph[node] = {};

import math


def file_to_graph (filename:str,type:str) -> dict:
	file = open(filename,"r")
	graph_final = {}
	for line in file:
		line = line.replace("\n","")
		aux = line.split(" ")
		if aux[0] not in graph_final:
			graph_final[aux[0]] = {}
			graph_final[aux[0]][aux[1]] = aux[2]
		else:
			graph_final[aux[0]][aux[1]] = aux[2]
	file.close()
	print(graph_final)
	return graph_final
# no duplicates concatenation
def concatenate_lists_nr (list1:list,list2:list):
	for item in list2:
		if item not in list1:
			list1.append(item)
	return list1
def is_empty (list:list):
	if not list:
		return True
	return False
class Graph:
	def __init__ (self,graph: dict={}) -> None:
		self.graph = graph
	def add_node(self,node) -> None:
		if node not in self.graph:
			self.graph[node] = {}
		else:
			pass
	def add_edge(self,node1,node2,cost) -> None:
		if node1 not in self.graph:
			self.graph[node1] = {}
		else:
			self.graph[node1][node2] = cost
	def return_nodes(self,nodes) -> list:
		return self.graph.keys()
	def return_neighbourhood (self,node) -> list:
		list1 = []
		try:
			for item in self.graph[node].keys():
				list1.append(item)
		except:
			return []
		return list1
	def return_neighbourhood_w_costs (self,node) -> dict:
		return self.graph[node]
	def bfs (self,initialNode,finalNode) -> None:
		if initialNode not in self.graph.keys():
			print (initialNode+" is a invalid inital node")
			return None
		isvisited = {initialNode}
		print("Visited node: "+initialNode)
		done = False
		actualnb = self.return_neighbourhood(initialNode)
		while (done==False):
			for node in actualnb:
				if (is_empty(actualnb)):
					done = True
					break
				elif (node == finalNode):
					print("Visited desired node: "+node)
					done = True
					break
				elif node not in isvisited: 
					isvisited.add(node)
					print("Visited node: "+node)
					actualnb.remove(node)
					actualnb = concatenate_lists_nr(actualnb,self.return_neighbourhood(node))
	def do_dfs(self,isvisited:set,nodeI,finalNode):
		if (nodeI==finalNode):
			return
		if node not in isvisited:
			print("Visited: "+node)
			isvisited.add(node)
			for neighbour in self.return_neighbourhood(nodeI):
				do_dfs(isvisited,neighbour,finalNode)

	def dfs(self,initialNode:str,finalNode:str) -> None:
		isvisited = set()
		do_dfs(isvisited,initialNode,finalNode)
		return
	def return_predecessors(self,distances:dict):
        pred = {node: None for node in self.graph}
        for node,distance in distances.items():
            for neighbor,cost in self.graph[node].items():
                if distances[neighbor] == distance+cost:
                    pred[neighbor] = node
        return pred
	def shortest_path(self,initialNode:str,finalNode:str)->None:
		

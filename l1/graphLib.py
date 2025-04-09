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
def concatenate_lists (list1:list,list2:list):
	for item in list2:
		list1.append(item)
	return list1
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
		return self.graph[node].keys()
	def return_neighbourhood_w_costs (self,node) -> dict:
		return self.graph[node]
	def bfs (self,initialNode,finalNode) -> list:
		isvisited = {}
		done = False
		actualnb = return_neighbourhood(initialNode)
		while (done==False):
			for node in actualnb:
				if (node == finalNode):
					done = true
				elif node not in isvisited:
					isvisited.add(node)
					print("Visited node: "+node)
					actualnb.remove(node)
					actualnb = concatenate_lists(actualnb,return_neighbourhood(node))


import math
import heapq
import time
from collections import deque

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
		if type=="undirectional":
			if aux[1] not in graph_final:
				graph_final[aux[1]] = {}
				graph_final[aux[1]][aux[0]] = aux[2]
			else:
				graph_final[aux[1]][aux[0]] = aux[2]
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
	def return_neighborhood (self,node) -> list:
		list1 = []
		try:
			for item in self.graph[node].keys():
				list1.append(item)
		except:
			return []
		return list1
	def return_neighborhood_w_costs (self,node) -> dict:
		return self.graph[node]
	def reconstruct_path(self,came_from, node):
	    path = []
	    while node:
	        path.append(node)
	        node = came_from.get(node)
	    return path[::-1]
	def bfs(start, goal):
	    queue = deque([start,None])
	    reverse_path = {}
	    visited = set()
	    exp_nodes = 0
	    start_time = time.time()
	def do_dfs(self,isvisited:set,nodeI,finalNode):
		if (nodeI==finalNode):
			return
		if nodeI not in isvisited:
			print("Visited: "+nodeI)
			isvisited.add(nodeI)
			for neighbor in self.return_neighborhood(nodeI):
				self.do_dfs(isvisited,neighbor,finalNode)

	def dfs(self,initialNode:str,finalNode:str) -> None:
		isvisited = set()
		self.do_dfs(isvisited,initialNode,finalNode)
		return
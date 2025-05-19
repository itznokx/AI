import graphlib as gl

graph1 = gl.Graph(gl.file_to_graph("qst1_graph.txt","undirectional"))
print(graph1.bfs("A","E"))

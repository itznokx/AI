import graphLib as gl

graph1 = gl.Graph(gl.file_to_graph("qst1_graph.txt","directional"))
graph1.dfs("A","G")

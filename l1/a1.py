import graphLib as gl

graph1 = gl.Graph(gl.file_to_graph("test.txt","directional"))
graph1.bfs("6","1")
from graphLibrary import Graph
def q1():
    g1 = Graph()
    g1.get_file_graph("q1l1.txt")
    path = g1.short_path("B","F")
    for x in path:
        print(x)
def main ():
    q1()
main()

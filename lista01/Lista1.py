from graphLibrary import Graph
def q1():
    g1 = Graph()
    g1.get_file_graph("q1l1.txt")
    g1.print_graph()
    g1.print_distances("B")
    g1.short_path("B","F")
def main ():
    q1()
main()

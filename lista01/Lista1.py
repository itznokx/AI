from graphLibrary import Graph
def q1():
    g1 = Graph()
    g1.get_file_graph("q1l1.txt")
    g1.print_graph()
    g1.short_path("B","F")
def q2():
    currency = [1,2,5,10,20,50,100]
    price = 70
    change = 30
    g2 = Graph()
    g2.returnChange(change,currency)
def main ():
    q1()
    q2()
main()

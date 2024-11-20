from graphLibrary import Graph
def getHeuristics():
    heuristics = {}
    file = open("heuristics.txt")
    for line in file.readlines():
        node_h_val = line.split()
        heuristics[node_h_val[0]] = int(node_h_val[1])
    return heuristics
def getCity():
    city = {}
    citiesCode = {}
    f = open("cities.txt")
    j = 1
    for i in f.readlines():
            node_city_val = i.split()
            city[node_city_val[0]] = [int(node_city_val[1]), int(node_city_val[2])]
            citiesCode[j] = node_city_val[0]
            j += 1
    return city, citiesCode
def create_city_graph():
    graph={}
    file = open("citiesGraph.txt")
    for i in file.readlines():
        node_val = i.split()
        if node_val[0] in graph and node_val[1] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0]: c})

            c = graph.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})
        elif node_val[0] in graph:
            c = graph.get(node_val[0])
            c.append([node_val[1], node_val[2]])
            graph.update({node_val[0]: c})
            graph[node_val[1]] = [[node_val[0], node_val[2]]]
        elif node_val[1] in graph:
            c = graph.get(node_val[1])
            c.append([node_val[0], node_val[2]])
            graph.update({node_val[1]: c})
            graph[node_val[0]] = [[node_val[1], node_val[2]]]
        else:
            graph[node_val[0]] = [[node_val[1], node_val[2]]]
            graph[node_val[1]] = [[node_val[0], node_val[2]]]
    return graph;
def GBFS(startNode, heuristics, graph, goalNode="Bucharest"):
    priorityQueue = queue.PriorityQueue()
    priorityQueue.put((heuristics[startNode], startNode))
    path = []
    while priorityQueue.empty() == False:
        current = priorityQueue.get()[1]
        path.append(current)
        if current == goalNode:
            break
        priorityQueue = queue.PriorityQueue()
        for i in graph[current]:
            if i[0] not in path:
                priorityQueue.put((heuristics[i[0]], i[0]))
    return path
def Astar(startNode, heuristics, graph, goalNode="Bucharest"):
    priorityQueue = queue.PriorityQueue()
    distance = 0
    path = []
    priorityQueue.put((heuristics[startNode] + distance, [startNode, 0]))
    while priorityQueue.empty() == False:
        current = priorityQueue.get()[1]
        path.append(current[0])
        distance += int(current[1])
        if current[0] == goalNode:
            break
        priorityQueue = queue.PriorityQueue()
        for i in graph[current[0]]:
            if i[0] not in path:
                priorityQueue.put((heuristics[i[0]] + int(i[1]) + distance, i))
    return path;
def print_path(path):
    for x in path:
        print(x)
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
def q3():
    heuristic = getHeuristics()
    graph = create_city_graph()
    city, citiesCode = getCity()
    for i, j in citiesCode.items():
        print(i, j)
    while True:
        inputCode = int(input("Please enter your desired city's number (0 for exit):"))
        if inputCode == 0:
            break
    cityName = citiesCode[inputCode]
    gbfs = GBFS(cityName, heuristic, graph)
    astar = Astar(cityName, heuristic, graph)
    print("GBFS => ", gbfs)
    print("ASTAR => ", astar)
def main ():
    q1()
    q2()
    q3()
main()

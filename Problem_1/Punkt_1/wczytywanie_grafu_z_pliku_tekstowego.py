def read_graph_from_file(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            u, v, capacity = map(int, line.strip().split())
            if u not in graph:
                graph[u] = {}
            graph[u][v] = capacity
    return graph


filename = 'graph.txt'
graph = read_graph_from_file(filename)
print("Graf, ktory jest pobrany z pliku:", graph)

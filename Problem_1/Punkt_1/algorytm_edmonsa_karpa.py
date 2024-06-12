import tworzenie_sieci_rezydualnej
from collections import deque

#plik "wczytywanie_grafu_z_pliku_tekstowego"
def ReadGraphFromFile(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            u, v, capacity = map(int, line.strip().split())
            if u not in graph:
                graph[u] = {}
            graph[u][v] = capacity
    return graph

filename = 'graph.txt'
graph = ReadGraphFromFile(filename)
print("Graf, ktory jest pobrany z pliku:", graph)

#plik "wczytywanie_grafu_z_pliku_tekstowego"
def Bfs(residual_graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()

        for v, capacity in residual_graph[u].items():
            if v not in visited and capacity > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True

    return False



def EdmondsKarp(graph, source, sink):
    residual_graph = tworzenie_sieci_rezydualnej.ResidualGraph(graph).BuildResidualGraph()
    parent = {}
    max_flow = 0

    while Bfs(residual_graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

    return max_flow

#przykladowe wywolanie funkcji
source = 0  # zakladajac, że 0 to źródło
sink = 3    # zakladajac, że 3 to ujście
max_flow_value = EdmondsKarp(graph, source, sink)
print("Maksymalny przeplyw (dzieki algorytmu Edmonsa-Karpa):", max_flow_value)

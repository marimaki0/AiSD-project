from algorytm_edmonsa_karpa import edmondsKarp

#w tym kodzie jest konwertacja z grafu
#dwudzielnego na siec przeplywowa
#a potem znajduje maksymalny przepływ
#za pomoca alg. Edmonsa-Karpa

def bipartiteToFlowGraph(bipartite_graph, X, Y):
    flow_graph = {}

    #dodawanie wierzcholku zrodlowego `s` jako 0-ego
    flow_graph[0] = {x: 1 for x in X}

    #odawanie wierzcholku ujsiowego `t` jako n+1, gdzie `n` jest najwiekszym wierzcholkiem w X lub Y
    t = max(max(X), max(Y)) + 1
    for y in Y:
        if y not in flow_graph:
            flow_graph[y] = {}
        flow_graph[y][t] = 1

    #dodawanie krawedzi z grafu dwudzielnego
    for x in X:
        if x not in flow_graph:
            flow_graph[x] = {}
        for y in bipartite_graph[x]:
            flow_graph[x][y] = 1

    return flow_graph, t

#przyk. dane wejsciowe dla grafu dwudzielnego
bipartite_graph = {
    1: [4, 5],
    2: [4],
    3: [5, 6],
    7: [5],
    8: [6]
}
X = [1, 2, 3, 7, 8]
Y = [4, 5, 6]

flow_graph, t = bipartiteToFlowGraph(bipartite_graph, X, Y)
max_matching = edmondsKarp(flow_graph, 0, t)
print("Maksymalne skojarzenie w grafie dwudzielnym:", max_matching)

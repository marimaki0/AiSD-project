#zle dziala, trzeba naprzwic
import matplotlib.pyplot as plt
from collections import defaultdict

def ReadGraphFromFile(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            u, v, capacity = map(int, line.strip().split())
            if u not in graph:
                graph[u] = {}
            graph[u][v] = capacity
    return graph

def draw_graph(graph, residual_graph=None, source=None, sink=None):
    plt.figure(figsize=(10, 8))
    pos = {}
    
    
    node_count = len(graph)
    for i, node in enumerate(graph):
        pos[node] = (i % 3, i // 3)
    
    
    all_nodes = set(graph.keys())
    for edges in graph.values():
        all_nodes.update(edges.keys())
    for node in all_nodes:
        if node not in pos:
            pos[node] = (len(pos) % 3, len(pos) // 3)
    
    for u in graph:
        for v in graph[u]:
            color = 'r' if residual_graph and residual_graph[u][v] != graph[u][v] else 'b'
            plt.arrow(pos[u][0], pos[u][1], pos[v][0] - pos[u][0], pos[v][1] - pos[u][1],
                      head_width=0.1, head_length=0.1, fc=color, ec=color)
            plt.text((pos[u][0] + pos[v][0]) / 2, (pos[u][1] + pos[v][1]) / 2, str(graph[u][v]), color="g", fontsize=12)
    
    for node in pos:
        plt.scatter(pos[node][0], pos[node][1], s=100)
        plt.text(pos[node][0], pos[node][1], str(node), fontsize=12, ha='right')
    
    plt.xlabel('Nodes')
    plt.ylabel('Flow')
    plt.title('Network Flow')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    filename = 'graph.txt'
    graph = ReadGraphFromFile(filename)
    print("Graf, ktory jest pobrany z pliku:", graph)

    source = 0
    sink = 3
    draw_graph(graph)
    max_flow_value = EdmondsKarp(graph, source, sink)
    print("Maksymalny przeplyw (dzieki algorytmu Edmonsa-Karpa):", max_flow_value)

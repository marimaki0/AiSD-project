import math
from collections import deque, defaultdict
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def DistanceBetween2Points(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

def Def(p1, p2, p3):
    return p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p2.y * p3.x - p1.y * p2.x - p3.y * p1.x

def Angle(point0, p):
    return math.atan2(p.y - point0.y, p.x - point0.x)

def Graham(points):
    if len(points) == 0:
        print("Nie ma punktow")
        return []
    
    point0 = min(points, key=lambda p: (p.y, p.x))
    sorted_points = sorted(points, key=lambda p: (Angle(point0, p), point0.DistanceBetween2Points(p)))
    stack = [point0, sorted_points[0]]

    for p in sorted_points[1:]:
        while len(stack) > 1 and Def(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)

    return stack

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
    residual_graph = defaultdict(dict)
    for u in graph:
        for v in graph[u]:
            residual_graph[u][v] = graph[u][v]
            residual_graph[v][u] = 0
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
    return max_flow, residual_graph

def draw_points(points, source, sink):
    x = [p.x for p in points]
    y = [p.y for p in points]
    plt.scatter(x, y, color='blue')
    for i, point in enumerate(points):
        if i == source:
            plt.scatter(point.x, point.y, color='yellow', edgecolor='black', marker='*', s=200, label='Fabryka')  # Fabryka jako żółta gwiazdka z czarną obwódką
        elif i == sink:
            plt.scatter(point.x, point.y, color='green', edgecolor='black', marker='o', s=100, label='Ujście')  # Ujście jako zielony okrąg z czarną obwódką
        else:
            plt.text(point.x, point.y, f'{i}', fontsize=8, ha='right')

def draw_convex_hull(convex_hull):
    x = [p.x for p in convex_hull]
    y = [p.y for p in convex_hull]
    plt.plot(x + [x[0]], y + [y[0]], 'k-', label='Otoczka wypukła')  # Otoczka wypukła w czarnym kolorze

def draw_graph(graph, points, source, sink, residual_graph):
    # Rysowanie krawędzi sieci przepływowej
    for u in graph:
        for v in graph[u]:
            if graph[u][v] > 0:
                if u == source:
                    plt.plot([points[source].x, points[v].x], [points[source].y, points[v].y], 'g-', label='Sieć przepływowa' if u == source and v == list(graph[u].keys())[0] else "")
                elif v == sink:
                    plt.plot([points[u].x, points[sink].x], [points[u].y, points[sink].y], 'g-', label='Sieć przepływowa' if u == list(graph.keys())[0] and v == sink else "")
                else:
                    plt.plot([points[u].x, points[v].x], [points[u].y, points[v].y], 'g-')
    
    # Podświetlenie ścieżek z przepływem
    for u in residual_graph:
        for v in residual_graph[u]:
            if v in graph[u] and residual_graph[u][v] < graph[u][v]:
                if u == source:
                    plt.plot([points[source].x, points[v].x], [points[source].y, points[v].y], 'r-', linewidth=2, alpha=0.5, label='Ścieżka przepływu' if 'Ścieżka przepływu' not in plt.gca().get_legend_handles_labels()[1] else "")
                elif v == sink:
                    plt.plot([points[u].x, points[sink].x], [points[u].y, points[sink].y], 'r-', linewidth=2, alpha=0.5, label='Ścieżka przepływu' if 'Ścieżka przepływu' not in plt.gca().get_legend_handles_labels()[1] else "")
                else:
                    plt.plot([points[u].x, points[v].x], [points[u].y, points[v].y], 'r-', linewidth=2, alpha=0.5)

def GetResult():
    points = GeneratePoints(0, -100, 100)
    
    if len(points) == 0:
        print("Nie ma punktow")
        return []

    return Graham(points)

import math
import random
from collections import deque, defaultdict

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
    point0 = min(points, key=lambda p: (p.y, p.x))
    points.remove(point0)
    points.sort(key=lambda p: (Angle(point0, p), point0.DistanceBetween2Points(p)))
    stack = [point0, points[0]]
    for p in points[1:]:
        while len(stack) > 1 and Def(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)
    return stack

def GeneratePoints(number, x_min, x_max, y_min, y_max):
    points = []
    for _ in range(number):
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        points.append(Point(x, y))
    return points

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
    return max_flow

if __name__ == "__main__":
    
    #generowanie losowych punktow
    points = GeneratePoints(10, 0, 10, 0, 10)
    print("Wygenerowane punkty: ")
    for point in points:
        print(point)

    #oblicznie otoczki wypuklej za pomoca alg. Grahama
    convex_hull = Graham(points)
    print("\nPunkty otoczki wypuklej: ")
    for point in convex_hull:
        print(point)

    #tworzymy graf z punktow otoczki wypuklej
    graph = defaultdict(dict)
    n = len(convex_hull)
    source = 0  #zakladamy ze 0 - zrodlo
    sink = n + 1  #nowe ujscie

    #dodawanie krawedzi miedzy fabryka a punktami otoczki
    for i in range(n):
        graph[source][i + 1] = 1 #przepustowosc 1 (relacja przyjzni)
        graph[i + 1][sink] = 1 #laczenie punktow otoczki z ujsciem

    #dodawamie krawedzi miedzy punktami otoczki z losowymi przepustowosciami (0 lub 1) 
    for i in range(n):
        for j in range(i + 1, n):
            capacity = random.choice([0, 1]) #losowe okreslenie czy sa przyjaciolmi (przepustowosc 1) czy nie (przepustowość 0)
            graph[i + 1][j + 1] = capacity
            graph[j + 1][i + 1] = capacity

    print("\nWygenerowany graf z losowymi przepustowosciami: ")
    for u in graph:
        for v in graph[u]:
            print(f"{u} -> {v} : {graph[u][v]}")

    #obliczenie maks. przeplywu przy pomocy alg. Edmondsa-Karpa
    max_flow_value = EdmondsKarp(graph, source, sink)
    print("\nMaksymalny przeplyw (algorytm Edmondsa-Karpa):", max_flow_value)

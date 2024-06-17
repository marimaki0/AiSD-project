import math
import random
from collections import deque, defaultdict
import matplotlib.pyplot as plt
import networkx as nx
import Problem_1.Punkt_2.otoczka_wypukla_grahama as p1

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
    
    # Generate random points
    points = GeneratePoints(10, 0, 100, 0, 100)
    print("Generated points: ")
    for point in points:
        print(point)

    # Compute the convex hull using Graham's algorithm
    convex_hull = Graham(points)
    print("\nConvex hull points: ")
    for point in convex_hull:
        print(point)
    
    # Visualization of points and convex hull
    plt.figure(figsize=(12, 6))
    
    # Plot the points
    plt.subplot(1, 2, 1)
    x_points = [point.x for point in points]
    y_points = [point.y for point in points]
    plt.scatter(x_points, y_points, color='blue')
    
    # Plot the convex hull
    convex_hull.append(convex_hull[0])  # to complete the hull
    hull_x = [point.x for point in convex_hull]
    hull_y = [point.y for point in convex_hull]
    plt.plot(hull_x, hull_y, color='red')

    for point in points:
        plt.text(point.x, point.y, f'({point.x}, {point.y})')

    plt.title('Otoczka wypukla')
    plt.xlabel('X')
    plt.ylabel('Y')

    # Create graph from convex hull points
    graph = defaultdict(dict)
    n = len(convex_hull)
    source = 0  # assuming 0 as source
    sink = n + 1  # new sink

    # Add edges from the source to the convex hull points and from points to the sink
    for i in range(n):
        graph[source][i + 1] = 1  # capacity 1 (friendship relation)
        graph[i + 1][sink] = 1  # connecting hull points to sink

    # Add edges between convex hull points with random capacities (0 or 1)
    for i in range(n):
        for j in range(i + 1, n):
            capacity = random.choice([0, 1])  # randomly decide if they are friends (capacity 1) or not (capacity 0)
            graph[i + 1][j + 1] = capacity
            graph[j + 1][i + 1] = capacity

    print("\nGenerated graph with random capacities: ")
    for u in graph:
        for v in graph[u]:
            print(f"{u} -> {v} : {graph[u][v]}")

    # Visualization of the graph with capacities
    plt.subplot(1, 2, 2)
    G = nx.DiGraph()
    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v, capacity=graph[u][v])
    
    # Use a larger value for the 'k' parameter in spring_layout to spread out the nodes
    pos = nx.spring_layout(G, k=2.0)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20)
    labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title('')
    plt.show()

    # Compute maximum flow using Edmonds-Karp algorithm
    max_flow_value = EdmondsKarp(graph, source, sink)
    print("\nMaximum flow (Edmonds-Karp algorithm):", max_flow_value)

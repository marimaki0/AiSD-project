import math
import random
from collections import deque, defaultdict

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def distance_between_2points(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

def det(p1, p2, p3):
    return p1.x * p2.y + p2.x * p3.y + p3.x * p1.y - p2.y * p3.x - p1.y * p2.x - p3.y * p1.x

def angle(point0, p):
    return math.atan2(p.y - point0.y, p.x - point0.x)

def graham(points):
    point0 = min(points, key=lambda p: (p.y, p.x))
    points.remove(point0)
    points.sort(key=lambda p: (angle(point0, p), point0.distance_between_2points(p)))
    stack = [point0, points[0]]
    for p in points[1:]:
        while len(stack) > 1 and det(stack[-2], stack[-1], p) <= 0:
            stack.pop()
        stack.append(p)
    return stack

def generate_points(number, x_min, x_max, y_min, y_max):
    points = []
    for _ in range(number):
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        points.append(Point(x, y))
    return points

def bfs(residual_graph, source, sink, parent):
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

def edmondsKarp(graph, source, sink):
    residual_graph = defaultdict(dict)
    for u in graph:
        for v in graph[u]:
            residual_graph[u][v] = graph[u][v]
            residual_graph[v][u] = 0
    parent = {}
    max_flow = 0
    while bfs(residual_graph, source, sink, parent):
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
    points = generate_points(10, 0, 10, 0, 10)
    print("Generated points:")
    for point in points:
        print(point)

    # Compute convex hull using Graham's scan
    convex_hull = graham(points)
    print("\nConvex Hull points:")
    for point in convex_hull:
        print(point)

    # Create graph from convex hull
    graph = defaultdict(dict)
    n = len(convex_hull)
    source = 0  # Assuming 0 is the source (factory)
    sink = n + 1  # New sink node

    # Add edges between the factory and the convex hull points
    for i in range(n):
        graph[source][i + 1] = 1  # Capacity of 1 (friend relationship)
        graph[i + 1][sink] = 1  # Connect hull points to sink

    # Add edges between hull points with random capacities (0 or 1)
    for i in range(n):
        for j in range(i + 1, n):
            capacity = random.choice([0, 1])  # Randomly decide if they are friends (capacity 1) or not (capacity 0)
            graph[i + 1][j + 1] = capacity
            graph[j + 1][i + 1] = capacity

    print("\nGenerated Graph with Random Capacities:")
    for u in graph:
        for v in graph[u]:
            print(f"{u} -> {v} : {graph[u][v]}")

    # Compute max flow using Edmonds-Karp algorithm
    max_flow_value = edmondsKarp(graph, source, sink)
    print("\nMax Flow (using Edmonds-Karp):", max_flow_value)

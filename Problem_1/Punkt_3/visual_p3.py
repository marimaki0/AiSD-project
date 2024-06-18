import random
from collections import deque, defaultdict
import matplotlib.pyplot as plt
import networkx as nx
from problem1_p3 import GeneratePoints
from problem1_p3 import Graham
from problem1_p3 import Point

def ReadPointsFromFile(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(int, line.split())
            points.append(Point(x, y))
    return points

def GetResult(custom_points):
    result = Graham(custom_points)
    return result

def Visualisation():
    points=ReadPointsFromFile("test1.txt")
    convex_hull=GetResult(points)

    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    x_points = [point.x for point in points]
    y_points = [point.y for point in points]
    plt.scatter(x_points, y_points, color='blue')
    
    convex_hull.append(convex_hull[0]) 
    hull_x = [point.x for point in convex_hull]
    hull_y = [point.y for point in convex_hull]
    plt.plot(hull_x, hull_y, color='red')

    for point in points:
        plt.text(point.x, point.y, f'({point.x}, {point.y})')

    plt.title('Otoczka wypukla')
    plt.xlabel('X')
    plt.ylabel('Y')

    graph = defaultdict(dict)
    n = len(convex_hull)
    source = 0 
    sink = n + 1 

    for i in range(n):
        graph[source][i + 1] = 1  
        graph[i + 1][sink] = 1 

    for i in range(n):
        for j in range(i + 1, n):
            capacity = random.choice([0, 1]) 
            graph[i + 1][j + 1] = capacity
            graph[j + 1][i + 1] = capacity

    plt.subplot(1, 2, 2)
    G = nx.DiGraph()
    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v, capacity=graph[u][v])
    
    pos = nx.spring_layout(G, k=2.0)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20)
    labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title('')
    plt.show()


if __name__ == "__main__":
    Visualisation()


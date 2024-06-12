from part3_with_vis import Point, Graham, EdmondsKarp, draw_points, draw_convex_hull, draw_graph, GetResult
import matplotlib.pyplot as plt
from collections import defaultdict
import random

def GenerateTestPoints():
    points = [
        Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3), Point(4, 4),
        Point(5, 5), Point(6, 6), Point(7, 7), Point(8, 8), Point(9, 9),
        Point(1, 8), Point(2, 7), Point(3, 6), Point(4, 5), Point(5, 4)
    ]
    return points

def TestGraham():
    points = GenerateTestPoints()
    convex_hull = Graham(points)
    print("\nPunkty otoczki wypukłej: ")
    for point in convex_hull:
        print(point)
    return convex_hull

def TestEdmondsKarp():
    points = GenerateTestPoints()
    convex_hull = Graham(points)

    # Dodanie fabryki (źródła) jako barycentrum otoczki wypukłej
    barycenter_x = sum(p.x for p in convex_hull) / len(convex_hull)
    barycenter_y = sum(p.y for p in convex_hull) / len(convex_hull)
    factory = Point(barycenter_x, barycenter_y)
    points.append(factory)

    # Dodanie ujścia jako dodatkowego punktu poza otoczką
    sink_point = Point(barycenter_x + 10, barycenter_y + 10)  # Ujście poza otoczką
    points.append(sink_point)

    # Tworzenie grafu z punktów otoczki wypukłej i wewnętrznych punktów
    graph = defaultdict(dict)
    n = len(points) - 2  # Ostatnie dwa punkty to fabryka i ujście
    source = n  # Źródło jest barycentrum
    sink = n + 1  # Nowe ujście jest dodatkowym punktem

    # Dodawanie krawędzi między fabryką a wewnętrznymi punktami
    for i in range(n):
        if points[i] not in convex_hull:  # Tylko wewnętrzne punkty
            graph[source][i] = 1  # Przepustowość 1 (relacja przyjaźni)

    # Dodawanie krawędzi między wewnętrznymi punktami a ujściem
    for i in range(n):
        if points[i] not in convex_hull:  # Tylko wewnętrzne punkty
            graph[i][sink] = 1  # Łączenie wewnętrznych punktów z ujściem

    # Dodawanie krawędzi między wewnętrznymi punktami z losowymi przepustowościami (0 lub 1)
    for i in range(n):
        for j in range(i + 1, n):
            if points[i] not in convex_hull and points[j] not in convex_hull:
                capacity = random.choice([0, 1])  # Losowe określenie czy są przyjaciółmi (przepustowość 1) czy nie (przepustowość 0)
                graph[i][j] = capacity
                graph[j][i] = capacity

    print("\nWygenerowany graf z losowymi przepustowościami: ")
    for u in graph:
        for v in graph[u]:
            print(f"{u} -> {v} : {graph[u][v]}")

    # Obliczanie maks. przepływu przy pomocy alg. Edmondsa-Karpa
    max_flow_value, residual_graph = EdmondsKarp(graph, source, sink)
    print("\nMaksymalny przepływ (algorytm Edmondsa-Karpa):", max_flow_value)

    # Rysowanie punktów, otoczki wypukłej i grafu przepływowego
    plt.figure(figsize=(12, 12))
    draw_points(points, source, sink)
    draw_convex_hull(convex_hull)
    draw_graph(graph, points, source, sink, residual_graph)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Punkty, Otoczka Wypukła i Graf Przepływowy')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    print("Testing Graham Algorithm")
    TestGraham()
    
    print("Testing Edmonds-Karp Algorithm")
    TestEdmondsKarp()

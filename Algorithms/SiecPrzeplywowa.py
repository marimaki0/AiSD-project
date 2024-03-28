import pprint

graph = {}
values = {}
v = int(input("Enter number of vertices: "))

print("Enter vertices(keys) : ")
for i in range(v):
    graph.setdefault(input())

edges = {}
for x in graph:
    edges.setdefault(x)

for i in graph:
    graph[i] = edges.copy()

print("Enter weights: ")
for i in graph:
    print(i)
    for j in graph[i]:
        print(i + " : " +j)
        var = input()
        graph[i][j] = var

pprint.pprint(graph)
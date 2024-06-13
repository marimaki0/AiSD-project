class ResidualGraph:
    def __init__(self, graph):
        self.graph = graph
        self.residual_graph = {}

    def BuildResidualGraph(self):
        for u in self.graph:
            for v, capacity in self.graph[u].items():
                if u not in self.residual_graph:
                    self.residual_graph[u] = {}
                if v not in self.residual_graph:
                    self.residual_graph[v] = {}
                self.residual_graph[u][v] = capacity
                self.residual_graph[v][u] = 0 #!dodajemy krawedz w przeciwnym kierunku o pojemności 0
        return self.residual_graph

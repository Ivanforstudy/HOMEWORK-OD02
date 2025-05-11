class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))

g = Graph()

g.add_edge("Кошка", "Хомяк")
g.add_edge("Кошка", "Рыба")
g.add_edge("Собака", "Птица")
g.add_edge("Собака", "Рыба")
g.add_edge("Хомяк", "Мышь")
g.add_edge("Птица", "Черепаха")

g.print_graph()
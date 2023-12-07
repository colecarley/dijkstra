from graph import graph as g

def main():
    edges = [
        ("A", "C", 3),
        ("A", "F", 2),
        ("C", "F", 2),
        ("C", "E", 1),
        ("F", "E", 3),
        ("F", "G", 5),
        ("F", "B", 6),
        ("E", "B", 2),
        ("C", "D", 4),
        ("D", "B", 1),
        ("B", "G", 2),
    ]

    graph = g.Graph(7)

    for edge in edges:
        graph.add_edge(edge[0], edge[1], edge[2])
    path, distance = graph.shortest_path("A", "B")

    print(path, distance)

main()
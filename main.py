from graph import graph as g

def main():
    edges = [
        ("A", "B", 1),
        ("A", "C", 2),
        ("B", "K", 3), 
        ("B", "L", 3),
        ("C", "M", 1),
        ("C", "H", 1),
        ("C", "D", 2),
        ("C", "F", 17),
        ("H", "M", 1),
        ("H", "D", 4),
        ("D", "L", 2),
        ("D", "E", 9),
        ("D", "F", 7),
        ("L", "K", 3),
        ("K", "F", 1),
        ("K", "E", 9),
        ("F", "E", 2),
        ("F", "N", 4),
        ("F", "I", 7),
        ("F", "O", 1),
        ("E", "G", 5),
        ("G", "N", 6),
        ("G", "I", 5),
        ("G", "J", 2),
        ("N", "I", 3),
        ("O", "J", 2),
        ("J", "I", 6),
    ]

    nodes = set()
    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])

    graph = g.Graph(len(nodes))

    for edge in edges:
        graph.add_edge(edge[0], edge[1], edge[2])
    path, distance = graph.shortest_path("A", "I")

    print(path, distance)

main()
import math
from typing import Generic, TypeVar

T = TypeVar('T')

# graph class - vertices can be of any type
class Graph(Generic[T]):
    matrix: list[list[T]] = [] # Adjacency matrix
    vertices: list[T] = [] # List of vertices
    size = 0 # Number of possible vertices

    def __init__(self, size: int):
        self.matrix = [[math.inf for _ in range(size)] for _ in range(size)]
        self.size = size

    def add_edge(self, vertex1: T, vertex2: T, weight = 1):
        if vertex1 not in self.vertices:
            self.vertices.append(vertex1)

        if vertex2 not in self.vertices:
            self.vertices.append(vertex2)

        first: int = self.vertices.index(vertex1)
        second: int = self.vertices.index(vertex2)

        self.matrix[first][second] = weight
        self.matrix[second][first] = weight


    def remove_edge(self, vertex1: T, vertex2: T):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            return None
        first: int = self.vertices.index(vertex1)
        second: int = self.vertices.index(vertex2)

        self.matrix[first][second] = 0
        self.matrix[second][first] = 0


    def count_edges_at(self, vertex: T):
        if vertex not in self.vertices:
            return None
        index: int = self.vertices.index(vertex)
        count: int = 0

        for i in range(self.size):
            if self.matrix[index][i] != math.inf:
                count += 1

        return count
    
    def get_edge_weight(self, vertex1: T, vertex2: T):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            return None
        
        first: int = self.vertices.index(vertex1)
        second: int = self.vertices.index(vertex2)

        return self.matrix[first][second]
    
    def get_neighbors(self, vertex: T):
        if vertex not in self.vertices:
            return None
        
        index: int = self.vertices.index(vertex)

        neighbors: list[T] = []
        for i in range(self.size):
            if self.matrix[index][i] != math.inf:
                neighbors.append(self.vertices[i])

        return neighbors
            
    def shortest_path(self, start: T, end: T) -> tuple[list[T], int]:
        if start not in self.vertices or end not in self.vertices:
            return None

        distances: list[int] = [math.inf for _ in range(self.size)]
        distances[self.vertices.index(start)] = 0
        explored: set[T] = set()

        previous: dict[T, T | None] = {
            start: None
        }

        shortest: int = math.inf
        current: T = start
        while True:
            explored.add(current)
            # update distances
            for neighbor in self.get_neighbors(current):
                if neighbor not in explored:
                    weight = self.get_edge_weight(current, neighbor)
                    distance = distances[self.vertices.index(current)] + weight
                    if distance < distances[self.vertices.index(neighbor)]:
                        distances[self.vertices.index(neighbor)] = distance
                        previous[neighbor] = current

            # check if we're done
            if current == end:
                shortest = distances[self.vertices.index(end)]
                break

            # find next node
            p: T = current
            min_distance: int = math.inf
            for neighbor in self.get_neighbors(current):
                if neighbor not in explored:
                    if distances[self.vertices.index(neighbor)] < min_distance:
                        min_distance = distances[self.vertices.index(neighbor)]
                        current = neighbor
            if current == p:
                current = previous[current]

        # find path
        path: list[T] = []
        while current != None:
            path.append(current)
            current = previous[current]

        path.reverse()
        return path, shortest
        


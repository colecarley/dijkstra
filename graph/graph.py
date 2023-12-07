import math

# graph class - vertices can be of any type
class Graph:
    matrix = [] # Adjacency matrix
    vertices = [] # List of vertices
    size = 0 # Number of possible vertices

    def __init__(self, size):
        self.matrix = [[math.inf for _ in range(size)] for _ in range(size)]
        self.size = size

    def add_edge(self, vertex1, vertex2, weight = 1):
        if vertex1 not in self.vertices:
            self.vertices.append(vertex1)

        if vertex2 not in self.vertices:
            self.vertices.append(vertex2)

        first = self.vertices.index(vertex1)
        second = self.vertices.index(vertex2)

        self.matrix[first][second] = weight
        self.matrix[second][first] = weight


    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            return None
        first = self.vertices.index(vertex1)
        second = self.vertices.index(vertex2)

        self.matrix[first][second] = 0
        self.matrix[second][first] = 0


    def count_edges_at(self, vertex):
        if vertex not in self.vertices:
            return None
        index = self.vertices.index(vertex)
        count = 0

        for i in range(self.size):
            if self.matrix[index][i] != math.inf:
                count += 1

        return count
    
    def get_edge_weight(self, vertex1, vertex2):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            return None
        
        first = self.vertices.index(vertex1)
        second = self.vertices.index(vertex2)

        return self.matrix[first][second]
    
    def get_neighbors(self, vertex):
        if vertex not in self.vertices:
            return None
        
        index = self.vertices.index(vertex)

        neighbors = []
        for i in range(self.size):
            if self.matrix[index][i] != math.inf:
                neighbors.append(self.vertices[i])

        return neighbors
            
    def shortest_path(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return None

        distances = [math.inf for _ in range(self.size)]
        distances[self.vertices.index(start)] = 0
        explored = set()

        previous = {
            start: None
        }

        shortest = math.inf
        current = start
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
            min_distance = math.inf
            for neighbor in self.get_neighbors(current):
                if neighbor not in explored:
                    if distances[self.vertices.index(neighbor)] < min_distance:
                        min_distance = distances[self.vertices.index(neighbor)]
                        current = neighbor
            

        # find path
        path = []
        while current != None:
            path.append(current)
            current = previous[current]

        path.reverse()

        return path, shortest
        


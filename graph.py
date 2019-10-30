from node import Node
from priorityq import Queue


class Graph:

    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)
        self.nodes = [Node(i) for i in range(self.size)]

        for i, node in enumerate(self.nodes):
            for j, neighbor in enumerate(self.nodes):
                if self.matrix[i][j]:
                    node.neighbors.append(neighbor)

    def get_cost(self, node_a, node_b):
        return self.matrix[node_a.name][node_b.name]

    def dijkstra(self, start, end):
        current = self.nodes[start]
        end = self.nodes[end]
        current.cost = 0
        queue = Queue(current)

        while end.is_open:
            for neighbor in current.neighbors:
                if neighbor.is_open:
                    cost = self.get_cost(current, neighbor) + current.cost
                    if cost < neighbor.cost:
                        neighbor.cost = cost
                        neighbor.came_from = current
                    queue.add(neighbor)
            current.close()
            current = queue.pop()

        path = [current.name]
        while current.came_from:
            current = current.came_from
            path.insert(0, current.name)

        return ' '.join([str(n) for n in path]), end.cost

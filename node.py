class Node:

    def __init__(self, name):
        self.name = name
        self.cost = float('inf')
        self.came_from = None
        self.neighbors = []
        self.is_open = True

    def close(self):
        self.is_open = False

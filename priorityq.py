class Queue:

    def __init__(self, start):
        self.nodes = [start]

    def add(self, new):
        for i, node in enumerate(self.nodes):
            if new.cost < node.cost:
                self.nodes.insert(i, new)
                return
        else:
            self.nodes.append(new)

    def pop(self):
        return self.nodes.pop(0)

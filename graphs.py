class Queue(object):
    def __init__(self, values):
        self.values = values

    def remove(self):
        return self.values.pop()

    def add(self, value):
        self.values.insert(0, value)

    def get(self):
        return self.values[-1]

class Node(object):
    def __init__(self, value, nodes=[], visited=False):
        self.value = value 
        self.nodes = nodes
        self.visited = visited

    def DepthFirstSearch(self, root):
        if root is None:
            return
        print(root.value)
        root.visited = True
        for node in root.nodes:
            if not node.visited:
                self.DepthFirstSearch(root)
    
    def BreadthFirstSearch(self, root):
        queue = Queue([])
        root.visited = True
        queue.add(root)

        while len(queue.values) != 0:
            r = queue.remove()
            print(r.value)
            for node in r.nodes:
                if not node.visited:
                    node.visited = True
                    queue.add(node)
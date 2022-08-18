class Node(object):
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right 
        self.value = value 

    def sum_tree(self, start):
        if start.right == None and start.left == None:
            print(start.value)
            return start.value
        elif start.right == None:
            return start.value + self.sum_tree(start.left)
        elif start.left == None:
            print(start.value)
            return start.value + self.sum_tree(start.right)
        else:
            print(start.value)
            return start.value + self.sum_tree(start.left) + self.sum_tree(start.right)

    #Prints binary tree in ascending order
    #For pre order, the print is before the left and right 
    #For post order, the print is after the left and right
    def in_order_traversal(self, start):
        node = start
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.value)
            self.in_order_traversal(node.right)
        return start 




    
            


tree = Node(5, Node(4, Node(2), Node(6)), Node(3, Node(2)))

#print(tree.sum_tree(tree))
print(tree.flatten(tree))

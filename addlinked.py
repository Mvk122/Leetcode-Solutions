from re import L


class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        current = self
        total = []
        while current!= None:
            total.append(current.val)
            current = current.next
        return str(total)

def reverse(start):
    prev = None
    current = start
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev

def addTwoNumbers(l1, l2):
    def get_int(l):
        current = l
        total = ""
        while current != None:
            total += str(current.val)
            current = current.next
        return int(total)

    def str_to_linked(string):
        if len(string) == 1:
            return Node(int(string))
        else:
            return Node(int(string[0]), str_to_linked(string[1:]))

    total = str(get_int(l1) + get_int(l2))
    return str_to_linked(total)
    
    
list1 = Node(1, Node(2, Node(3, Node(4))))
list2 = Node(1, Node(9, Node(4, Node(8))))
print(list1)
print(addTwoNumbers(list1, list2))

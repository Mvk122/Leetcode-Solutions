class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data)

        node = node.next

        if node:
            print(sep)

def insertNodeAtPosition(llist, data, position):
    next_item = llist.next
    for i in range(position-3):
        next_item = next_item.next
    new_next = SinglyLinkedListNode(data)
    to_link = next_item.next
    next_item.next = new_next
    new_next.next = to_link

l = [1,2,3,4]
llist = SinglyLinkedList()
for element in l:
    llist.insert_node(element)

insertNodeAtPosition(llist.head, 5 , 2)

print_singly_linked_list(llist.head, '')
class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

    def __str__(self):
        nxt = None if self.next == None else self.next.data
        prev = None if self.prev == None else self.prev.data
        return f'value: {self.data} next: {nxt} prev: {prev}'

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep):
    while node:
        print(node.data)

        node = node.next

        if node:
            print(sep)

def sortedInsert(llist, data):
    current = llist
    if current.data > data:
        new_entry = DoublyLinkedListNode(data)
        new_entry.next = current
        current.prev = new_entry
        return new_entry
    while True:
        if current.next == None:
            new_entry = DoublyLinkedListNode(data)
            current.next = new_entry
            new_entry.prev = current
            break
        elif data <= current.next.data and data >= current.data:
            new_entry = DoublyLinkedListNode(data)
            old_next = current.next
            current.next = new_entry
            new_entry.prev = current
            new_entry.next = old_next
            old_next.prev = new_entry
            break
        else:
            current = current.next
    return llist

def reverse(llist):
    current = llist.head
    while current is not None:
        temp = current.prev
        current.prev = current.next 
        current.next = temp
        current = current.prev
        print(current)

    if temp is not None:
        llist.head = temp.prev

    return llist



l = [1,3,5,8]

llist = DoublyLinkedList()

for element in l:
    llist.insert_node(element)

sortedInsert(llist.head, 4)
pointer = reverse(llist)

print_doubly_linked_list(pointer, '')
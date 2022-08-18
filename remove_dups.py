class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insert_node(self, node_data):
        node = ListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def deleteDuplicates(head):
        current = head
        while current is not None:
            if current.next is None:
                return head
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head



def print_singly_linked_list(node, sep):
    while node:
        print(node.val)

        node = node.next

        if node:
            print(sep)

list = ListNode(1,ListNode(1,ListNode(2,ListNode(2,ListNode(3,ListNode(3))))))
list2 = ListNode(1, ListNode(1, ListNode(1)))
deleteDuplicates(list)
deleteDuplicates(list2)

print_singly_linked_list(list, ' ')
print_singly_linked_list(list2, ' ')

class Node(object):
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

    def add(self, val):
        self.next = Node(val)
        return self.next

    def __str__(self):
        current = self
        returnstr = ''
        while current.next != None:
            returnstr += f'{current.val} '
            current = current.next

        return returnstr

def merge_lists(l1, l2):
    new = []
    l1p = 0
    l2p = 0
    while l1p <= len(l1) or l2p <= len(l2):
        if l1[l1p] < l2[l2p]:
            new.append(l1[l1p])
            l1p += 1
        else:
            new.append(l2[l2p])
            l2p += 1
    return new


def merge_linked_lists(l1, l2):
    new = Node(-1)
    head = new
    while l1.next != None or l2.next != None:
        if l1.val < l2.val:
            new.next = Node(l1.val)
            l1 = l1.next
            new = new.next
        else:
            new.next = Node(l2.val)
            l2 = l2.next
            new = new.next

    return head

l1 = Node(2)
l1.add(3).add(4).add(5)
l2 = Node(1)
l2.add(3).add(4).add(6).add(7)


print(merge_lists([1,5,6], [2,4,8]))

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    mid = head
    end = head
    while end and end.next:
        mid = mid.next 
        end = end.next.next
    return mid

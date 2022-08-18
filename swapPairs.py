class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    f_head = head
    def swap(head, prev):
        prev.next = head.next
        temp = head.next.next
        head.next.next = head
        head.next = temp
        return head #head is now the prev

    if head.next is not None:
        temp = head.next.next
        head.next.next = head
        head.next = temp

    else:
        return head
    prev = head 
    head = head.next
    while head is not None:
        prev = swap(head, prev)
        head = prev.next
    return f_head





    

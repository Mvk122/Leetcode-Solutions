def reverseList(head):
    def reverseList_f(prev, head):
        if head is None:
            return prev
        elif head.next is None:
            head.next = prev
            return head
        else:
            temp = head.next
            head.next = prev
            return reverseList_f(head, temp)
    return reverseList_f(None, head)
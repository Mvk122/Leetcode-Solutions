from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = head
        if head is None:
            return head
        current = head.next
        while current: 
            if current.val == val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        if head.val == val:
            head = head.next
        return head
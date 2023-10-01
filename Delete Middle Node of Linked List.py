from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_prev = None
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow_prev = slow
            slow = slow.next
        if slow_prev is not None:
            slow_prev.next = slow.next
            return head
        if head is None:
            return head 
        return head.next
        
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_odd = head
        if head:
            even_start = head.next
            current_even = head.next
        else:
            return current_odd
        
        while current_odd and current_even:
            current_odd.next = current_even.next
            if current_odd.next:
                current_odd = current_odd.next
            if current_even and current_odd:
                current_even.next = current_odd.next
                current_even = current_even.next

        current_odd.next = even_start
        return head
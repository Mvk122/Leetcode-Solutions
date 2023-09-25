# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def add_nums(carry, left, right):
    total = carry + left + right
    new_carry = max(total - 10, 0) 
    if total > 9:
        return new_carry, total - 10
    else: 
        return new_carry, total

    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode(-1)
        yo = current
        carry = 0
        while (l1 is not None or l2 is not None):
            total = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + carry
            if total > 9:
                carry = 1
                total -= 10
            else:
                carry = 0
            
            if current is not None and current.val == -1: 
                current.val = total
            else:
                current.next = ListNode(total)
                current = current.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

            if l1 is None and l2 is None and carry == 1:
                current.next = ListNode(1)
                current = current.next
        return yo
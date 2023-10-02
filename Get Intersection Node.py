from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        seen_a = {}
        seen_b = {}
        while a:
            seen_a[id(a)] = a
            a = a.next
        while b:
            seen_b[id(b)] = b
            b = b.next
        for element in seen_a:
            if element in seen_b:
                return seen_a[element]
        return None

        


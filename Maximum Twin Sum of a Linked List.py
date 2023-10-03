from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        new_list = []
        current = head
        while current:
            new_list.append(current.val)
            current = current.next
        l = 0
        r = len(new_list) - 1
        highest = float('-inf')
        while l < r:
            highest = max(highest, new_list[l] + new_list[r])
            l += 1
            r -= 1
        return highest 
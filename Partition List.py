from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_list = ListNode(-1)
        larger_list = ListNode(-1)

        smaller_list_pointer = smaller_list
        larger_list_pointer = larger_list

        current = head
        while current:
            if current.val < x:
                smaller_list_pointer.next = current
                smaller_list_pointer = current
            else:
                larger_list_pointer.next = current
                larger_list_pointer = current
            current = current.next
        
        
        larger_list_pointer.next = None
        smaller_list_pointer.next = larger_list.next
        return smaller_list.next

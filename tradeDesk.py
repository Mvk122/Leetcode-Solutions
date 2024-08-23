# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None


def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
        
    return prev
    
def add_list_element(first, second, carry):
    first_value = first.value if first else 0
    second_value = second.value if second else 0
    
    temp = first_value + second_value + carry
    return ListNode(temp % 10000), temp // 10000

def solution(a, b):
    reversed_a = reverse_linked_list(a)
    reversed_b = reverse_linked_list(b)
    
    current_a, current_b = reversed_a, reversed_b
    new_head = None
    previous = None
    carry = 0
    
    while current_a or current_b:
        current, carry = add_list_element(current_a, current_b, carry)
        
        if previous:
            previous.next = current
            previous = current
        if new_head is None:
            new_head = current
            previous = current
        if current_a:
            current_a = current_a.next
        if current_b:
            current_b = current_b.next
            
    if carry:
        previous.next = ListNode(carry)
        
    new_head = reverse_linked_list(new_head)
    reverse_linked_list(reversed_a)
    reverse_linked_list(reversed_b)
    
    return new_head
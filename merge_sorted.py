class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_sorted(l1, l2):
    if l1.val < l2.val:
        main = l1
        sec = l2
    else:
        main = l2
        sec = l1
    main_head = main
    while main.next is not None or sec is not None:
        #print(f"l2 {print_singly_linked_list(l2, ' ')}")
        print(f"l1 {print_singly_linked_list(l1, ' ')}")
        if main.next.val > sec.val:
            temp = main.next
            main.next = sec
            sec = sec.next
            main.next.next = temp
            sec = sec.next
        else:
            sec = sec.next
    if main.next is None:
        main.next = sec
        return main_head
    if sec is None:
        return main_head

def print_singly_linked_list(node, sep):
    while node:
        print(node.val, end=sep)
        node = node.next
    print(" ")

def merge_sorted_reg(nums1, nums2, m, n):
    fp = 0 
    sp = 0

def merge_sorted_better(list1, list2):
    if not list1 and not list2:
        return None 
    if not list1:
        return list2
    if not list2: 
        return list1

    if list1.val <= list2.val:
        root = ListNode(list1.val, None)
        return merge_sorted_better(list1.next, list2)
    else:
        root = ListNode(list2.val, None)
        return merge_sorted_better(list1, list2.next)

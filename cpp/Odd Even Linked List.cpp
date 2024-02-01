#include "common.h"

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    // This does it by the value of the node and not by 
    // the index being odd or even
    ListNode* oddEvenList_by_value(ListNode* head) {
        ListNode* even_head = nullptr;
        ListNode* odd_head = nullptr;
        ListNode* current_even = even_head;
        ListNode* current_odd = odd_head;
        ListNode* current = head;

        while (current) {
            ListNode* next_node = current->next;
            current->next = nullptr;

            if (current->val % 2) {
                if (current_odd) {
                    current_odd->next = current;
                    current_odd = current;
                } else {
                    odd_head = current;
                    current_odd = odd_head;
                }
            } else {
                if (current_even) {
                    current_even->next = current;
                    current_even = current;
                } else {
                    even_head = current;
                    current_even = even_head;
                }
            }
            current = next_node;
        }
        if (current_odd) {
            current_odd->next = even_head; 
        }
        return odd_head ? odd_head : even_head;
    }

    
    ListNode* oddEvenList(ListNode* head) {
        if (!head) return nullptr;
        ListNode* odd = head;
        ListNode* even = head->next;
        ListNode* evenHead = even;

        while (even && even->next) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        odd->next = evenHead;
        return head;
    }


};
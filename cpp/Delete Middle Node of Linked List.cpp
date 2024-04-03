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
    ListNode* deleteMiddle(ListNode* head) {
        ListNode * slow_prev = nullptr;
        ListNode * slow = head;
        ListNode * fast = head;

        while (fast && fast->next) {
            fast = fast->next->next;
            slow_prev = slow;
            slow = slow->next;
        }
        if (slow_prev) {
            slow_prev->next = slow->next;
            return head;
        }
        if (!head) {
            return head;
        }
        return head->next;
    }
};
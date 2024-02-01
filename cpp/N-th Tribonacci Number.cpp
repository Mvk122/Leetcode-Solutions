#include "common.h"

class Solution {
public:
    int tribonacci_f(int n, unordered_map<int, int> &memo) {
        if (memo.count(n) > 0) {
            return memo[n];
        } else {
            int val = tribonacci_f(n-1, memo) + tribonacci_f(n-2, memo) + tribonacci_f(n-3, memo);
            memo[n] = val;
            return val;
        }
    }
    int tribonacci(int n) {
        unordered_map<int, int> memo = {{0, 0}, {1, 1}, {2, 1}};
        return tribonacci_f(n, memo);

    }
};
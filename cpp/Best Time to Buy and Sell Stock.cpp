#include "common.h"
#include "climits"

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowest_so_far = INT_MAX;
        int max_profit = 0;

        for (auto price : prices) {
            lowest_so_far = min(lowest_so_far, price);
            max_profit = max(price-lowest_so_far, max_profit);
        }
        return max_profit;
    }
};
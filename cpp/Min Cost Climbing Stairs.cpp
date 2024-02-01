#include "common.h"

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        if (cost.size() < 2) {
            return *min_element(cost.begin(), cost.end());
        }
        vector<int> cost_prev = {cost.back(), 0};

        for (int i=cost.size()-2; i > -1; i--) {
            int minimum_cost = cost[i] + min(cost_prev[0], cost_prev[1]);
            cost_prev[1] = cost_prev[0];
            cost_prev[0] = minimum_cost;
        }
        return *min_element(cost_prev.begin(), cost_prev.end());
    }
};
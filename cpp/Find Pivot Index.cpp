#include "common.h"

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        vector<int> leftSum = {0};
        vector<int> rightSum = {0};

        for (int i=1; i< nums.size(); i++) {
            leftSum.push_back(nums[i-1]+ leftSum.back());
        }

        for (int i=nums.size()-2; i >= 0; i--) {
            rightSum.push_back(nums[i+1] + rightSum.back());
        }
        for (int i=0; i < nums.size(); i++) {
            if (leftSum[i] == rightSum[nums.size()-i-1]) {
                return i;
            }
        }

        return -1;
    }
};
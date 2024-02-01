#include "common.h"

class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        if (nums.size() % 3 != 0) {
            return vector<vector<int>>();
        }
        sort(nums.begin(), nums.end());
        for (int i=0; i< nums.size(); i++) {
            if (i % 3 == 1 && nums[i] - nums[i-1] > k) {
                return vector<vector<int>>();
            } else if ((i % 3 == 2) && (nums[i] - nums[i-1] > k || nums[i] - nums[i-2] > k)) {
                return vector<vector<int>>();
            }
        }
        vector<vector<int>> ret;
        vector<int> current;
        for (int i=0; i<nums.size(); i++) {
            if (i%3==0) {
                if (i==0) {
                    current.push_back(nums[i]);
                } else {
                    ret.push_back(current);
                    current = vector<int>();
                    current.push_back(nums[i]);
                }
            } else {
                current.push_back(nums[i]);
            }
        }
        if (current.size() > 0) {
            ret.push_back(current);
        }
        return ret;
    }
};
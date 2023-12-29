#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        if (nums.size() == 1) {
            return nums[0];
        }
        int start_pointer = 0; 
        int end_pointer = 0;
        double current_value = 0;

        while (end_pointer < k) {
            current_value += nums[end_pointer];
            end_pointer++;
        }

        double highest_value = current_value;

        while (end_pointer < nums.size()) {
            current_value += nums[end_pointer] - nums[start_pointer];
            highest_value = max(current_value, highest_value);
            end_pointer++;
            start_pointer++;
        }
        return highest_value / k;
    }
};
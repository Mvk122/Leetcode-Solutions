#include <string>
#include <iostream>
#include <numeric>
#include <unordered_set>
#include <queue> 
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zeroes_found = 0;
        queue<int> zero_positions;

        for (int i=0; i<nums.size(); i++) {
            if (nums[i] == 0) {
                zero_positions.push(i);
                zeroes_found++;
            } else if (zero_positions.size() > 0) {
                int zero_pos = zero_positions.front();
                zero_positions.pop();
                nums[zero_pos] = nums[i];
                zero_positions.push(i);
            }
        }

        for (int i=nums.size()-zeroes_found; i< nums.size(); i++) {
            nums[i] = 0;
        }
    }
};
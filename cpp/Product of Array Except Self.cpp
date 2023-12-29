#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix_array(nums.size());
        prefix_array[0] = nums[0];
        
        vector<int> postfix_array(nums.size());
        postfix_array[nums.size()-1] = nums[nums.size()-1];

        for (int i=1; i<nums.size(); i++) {
            prefix_array[i] = prefix_array[i-1] * nums[i];
        }


        for (int i=nums.size()-2; i>-1; i--) {
            postfix_array[i] = postfix_array[i+1] * nums[i];
        }

        vector<int> result(nums.size());

        for (int i=0; i<nums.size(); i++) {
            if (i==0) {
                result[i] = postfix_array[1];
            } else if (i==nums.size()-1) {
                result[i] = prefix_array[nums.size()-2];
            } else {
                result[i] = prefix_array[i-1] * postfix_array[i+1];
            }
        }

        return result;
        

    }
};
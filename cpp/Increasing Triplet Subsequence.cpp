#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
using namespace std;



class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int first = INT_MAX;
        int second = INT_MAX;

        for (const auto n : nums) {
            if (n <= first) {
                first = n;
            } else if (n <= second) {
                second = n;
            } else {
                return true;
            }
        }
        return false;
    }
};
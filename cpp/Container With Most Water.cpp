#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;

        int max_water = 0;

        while (l<r) {
            max_water = max(max_water, (r-l)* min(height[l], height[r]));

            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return max_water;      
    }
};
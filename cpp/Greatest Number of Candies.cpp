#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int highest_candies = * max_element(candies.begin(), candies.end());

        vector<bool> highest(candies.size());
        for (int i=0; i< candies.size(); i++) {
            highest[i] = candies.at(i)+extraCandies >= highest_candies;
        }
        return highest;
    }
};
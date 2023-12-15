#include <string>
#include <iostream>
#include <numeric>
#include <unordered_set>
using namespace std;

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> in_nums_1(nums1.begin(), nums1.end());
        unordered_set<int> in_nums_2(nums2.begin(), nums2.end());

        vector<int> n1v;
        vector<int> n2v;

        for (const int& num: in_nums_1) {
            if (!in_nums_2.count(num)) {
                n1v.push_back(num);
            }
        }
        for (const int& num: in_nums_2) {
            if (!in_nums_1.count(num)) {
                n2v.push_back(num);
            }
        }

        vector<vector<int>> ret;
        ret.push_back(n1v);
        ret.push_back(n2v);

        return ret;

    }
};
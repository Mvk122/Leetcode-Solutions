#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
using namespace std;


class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> counter;
        int k_pairs = 0;

        for (const auto n: nums) {
            if (counter.count(n) > 0) {
                counter[n]++;
            } else {
                counter[n] = 1;
            }
        }

        for (const auto& pair: counter) {
            if (pair.first * 2 == k) {
                k_pairs += (pair.second / 2) * 2;
            } else if (counter.count(k-pair.first) > 0) {
                k_pairs += min(pair.second, counter[k-pair.first]);
            }
        }
        return k_pairs/2;
    }
};
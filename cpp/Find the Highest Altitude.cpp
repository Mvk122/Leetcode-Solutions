#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int current = 0;
        int highest = 0;

        for (const auto n: gain) {
            current += n;
            highest = max(current, highest);
        }

        return highest;
    }
};
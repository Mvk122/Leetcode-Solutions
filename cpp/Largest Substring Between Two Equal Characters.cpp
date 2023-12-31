#include <string>
#include <iostream>
#include <numeric>
#include <unordered_set>
#include <unordered_map>
#include <queue> 
using namespace std;

class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int highest = -1;
        unordered_map<char, int> first_positions;

        for (int i=0; i<s.size(); i++) {
            if (first_positions.count(s[i]) > 0) {
                highest = max(i - first_positions[s[i]]-1, highest);
            } else {
                first_positions[s[i]] = i;
            }
        }
        return highest;
    }
};
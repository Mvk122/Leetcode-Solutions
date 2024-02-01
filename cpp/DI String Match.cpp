#include "common.h"

class Solution {
public:
    vector<int> diStringMatch(string s) {
        int smallest_number = 0;
        vector<int> current = {0};

        for (const auto c: s) {
            if (c == 'D') {
                current.push_back(current.back()-1);
            } else {
                current.push_back(current.back()+1);
            }
            smallest_number = min(smallest_number, current.back());
        }

        if (smallest_number < 0) {
            for (int i=0; i<current.size(); i++) {
                current[i] = current[i] - smallest_number;
            }
        }
        return current;
    }
};
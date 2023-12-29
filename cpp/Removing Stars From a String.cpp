#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


class Solution {
public:
    string removeStars(string s) {
        string output = "";

        for (const auto c: s) {
            if (c != '*') {
                output += c;
            } else if (output.size() > 0) {
                output.pop_back();
            }
        }
        return output;
    }
};
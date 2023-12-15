#include <string>
#include <iostream>
#include <numeric>
#include <unordered_set>
#include <queue> 
using namespace std;

class Solution {
public:
    bool isContiguousSubsequence(string s, string t) {
        for (int i=0; i<t.size()-s.size(); i++) {
            int j = 0;

            while (t[i+j] == s[j]) {
                if (j == s.size()-1) {
                    return true;
                }
                j++;
            }
        }
        return false;
    }

    bool isSubsequence(string s, string t) {
        int s_pointer = 0;
        for (int i=0; i< t.size(); i++) {
            if (s[s_pointer] == t[i]) {
                s_pointer++;
            }
            if (s_pointer >= s.size()) {
                return true;
            }
        }
        return false;
    }
};
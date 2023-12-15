#include <string>
#include <iostream>
#include <numeric>
#include <unordered_set>
using namespace std;

class Solution {
public:
    static unordered_set<char> vowels;
    Solution() {
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
    }
    string reverseVowels(string s) {
        int left_ptr = 0;
        int right_ptr = s.size() -1;

        while (left_ptr < right_ptr) {
            if (vowels.count(s[left_ptr]) && vowels.count(s[right_ptr])) {
                swap(s[left_ptr], s[right_ptr]);
                left_ptr++;
                right_ptr--;
            } else if (vowels.count(s[left_ptr])) {
                right_ptr--;
            } else {
                left_ptr++;
            }
        }
        return s;
    }
};

unordered_set<char> Solution::vowels;
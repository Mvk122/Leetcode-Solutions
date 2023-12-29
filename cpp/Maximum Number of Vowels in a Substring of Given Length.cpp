#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxVowels(string s, int k) {
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};

        int start_pointer = 0;
        int end_pointer = 0;
        int current_vowels = 0;

        while (end_pointer <k) {
            if (vowels.count(s[end_pointer]) > 0) {
                current_vowels++;
            }
            end_pointer++;
        }
            int highest_vowels = current_vowels;

        while (end_pointer < s.size()) {
            start_pointer++;
            end_pointer++;

            if (vowels.count(s[end_pointer]) > 0) {
                current_vowels++;
            }
            if (vowels.count(s[start_pointer]) > 0) {
                current_vowels--;
            }
            highest_vowels = max(current_vowels, highest_vowels);
        }

        return highest_vowels;

    }
};
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    unordered_map<char, int> create_counter(string &word) {
        unordered_map<char, int> counter;
        for (const auto& c : word) {
            if (counter.contains(c)) {
                counter[c]++;
            } else {
                counter[c] = 1;
            }
        }
        return counter;
    }
    vector<string> commonChars(vector<string>& words) {
        auto first_word = this->create_counter(words[0]);
        
        if (words.size() > 1) {
            for (int i=1; i<words.size(); i++) {
                auto current_counter = this->create_counter(words[i]);
                for (const auto& c: current_counter) {
                    first_word[c.first] = min(c.second, first_word[c.first]);
                }
                for (const auto& c: first_word) {
                    first_word[c.first] = min(c.second, current_counter[c.first]);
                }
            }
        }

        vector<string> res;

        for (const auto& c: first_word) {
            for (int i=0; i<c.second; i++) {
                res.push_back(string(1, c.first));
            }
        }
        return res;
    }
};
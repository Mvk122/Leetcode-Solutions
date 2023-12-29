#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <iostream>
#include <algorithm>
using namespace std;


class Solution {
public:

    unordered_map<char, int> counter(string word) {
        unordered_map<char, int> result;

        for (const auto c: word) {
            if (result.count(c) > 0) {
                result[c]++;
            } else {
                result[c] = 1;
            }
        }

        return move(result);
    }

    template <typename T>
    multiset<int> numsByCounter(unordered_map<T, int> counter) {
        multiset<int> myset;
        
        for (const auto& pair: counter) {
            myset.insert(pair.second);
        }

        return move(myset);
    }

    bool closeStrings(string word1, string word2) {
        if (word1.size() != word2.size()) {
            return false;
        }     

        unordered_map<char, int> count1 = this->counter(word1);
        unordered_map<char, int> count2 = this->counter(word2);

        if (count1.size() != count2.size())  {
            return false;
        }

        for (const auto p: count1) {
            if (count2.count(p.first) < 1) {
                return false;
            }
        }

        multiset<int> set1 = this->numsByCounter(count1);
        multiset<int> set2 = this->numsByCounter(count2);

        return set1 == set2;
    }
};
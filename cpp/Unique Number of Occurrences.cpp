#include <string>
#include <iostream>
#include <numeric>
#include <unordered_set>
#include <unordered_map>
using namespace std;


class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> numbers;
        for (int i=0; i<arr.size(); i++) {
            if (numbers.count(arr[i]) > 0) {
                numbers[arr[i]]++;
            } else {
                numbers[arr[i]] = 1;
            }
        }

        unordered_set<int> stuff;
        for (const auto& pair: numbers) {
            if (stuff.count(pair.second)) {
                return false;
            } else {
                stuff.insert(pair.second);
            }
        }
        return true;
    }
};
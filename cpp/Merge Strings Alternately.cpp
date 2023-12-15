#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int w1p = 0;
        int w2p = 0;
        string result = "";
        while (word1.size() > w1p && word2.size() > w2p) {
            result += word1.at(w1p);
            result += word2.at(w2p);
            w1p++;
            w2p++;
        }
        if (w1p < word1.size()) {
            result += word1.substr(w1p, word1.size()+1);
        }  
        if (w2p < word2.size()) {
            result += word2.substr(w2p, word2.size()+1);
        }

        return result;
    }
};

int main() {
    Solution mySolution;
    cout << mySolution.mergeAlternately("cf", "eee") << "\n";
}
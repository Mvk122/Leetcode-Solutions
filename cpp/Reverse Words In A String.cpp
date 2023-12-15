#include <string>
#include <iostream>
#include <numeric>
#include <unordered_set>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
       vector<string> words;

       string current_word = "";

       for (int i=0; i<s.size(); i++) {
            if (s[i] == ' ') {
                if (current_word != "") {
                    words.push_back(current_word);
                }
                current_word = "";
            } else {
                current_word += s[i];
            }
       } 

       if (current_word != " ") {
        words.push_back(current_word);
       }
    
        copy(words.begin(), words.end(), std::ostream_iterator<string>(std::cout, " "));
        string output = "";
        for (int i = words.size() - 1; i >= 0; --i) {
            output += words[i];
            output += " ";
        }

        return output.substr(0, output.size()-1);
    
    }
};
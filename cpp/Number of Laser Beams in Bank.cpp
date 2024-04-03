#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
using namespace std;

class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int previous_devices = 0;
        
        int full_total = 0;

        for (auto b: bank) {
            int current_devices = 0;
            for (const char c: b) {
                if (c == '1') {
                    current_devices++;
                }
            }
            full_total += current_devices * previous_devices;
            if (current_devices > 0) {
                previous_devices = current_devices;
            }
        }
        return full_total;

    }
};
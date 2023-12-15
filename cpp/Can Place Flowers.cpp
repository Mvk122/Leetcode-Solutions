#include <string>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int flowersplaced = 0;
        for (int i=0; i< flowerbed.size(); i++) {
            if (i==0) {
                if (flowerbed.size() == 1) {
                    if (flowerbed[i] == 0) {
                        flowersplaced++;
                        flowerbed[i] = 1;
                    }
                } else if (flowerbed[i] == 0 && flowerbed[i+1] == 0) {
                    flowersplaced++;
                    flowerbed[i] = 1;
                }
            } else if (i==flowerbed.size()-1) {
                if (flowerbed[i]==0 && flowerbed[i-1]==0) {
                    flowersplaced++;
                    flowerbed[i] = 1;
                }
            } else if (flowerbed[i] == 0 && flowerbed[i-1]==0 && flowerbed[i+1] == 0) {
                flowersplaced += 1;
                flowerbed[i] = 1;
            }
        }
        return flowersplaced >= n;
    }
};
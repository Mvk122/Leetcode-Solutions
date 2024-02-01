#include "common.h"
#include <stack>

class Solution {
public:
    void collideAsteroid(int asteroid, vector<int> &asteroid_stack) {
        while (true) {
            if (asteroid_stack.size() == 0) {
                asteroid_stack.push_back(asteroid);
                return;
            } else if (asteroid_stack.back() > 0 && asteroid < 0) {
                if (abs(asteroid) == abs(asteroid_stack.back())) {
                    asteroid_stack.pop_back();
                    return;
                } else if (abs(asteroid) > abs(asteroid_stack.back())) {
                    asteroid_stack.pop_back();
                } else {
                    return;
                }
            } else {
                asteroid_stack.push_back(asteroid);
                return;
            }
        }
    }

    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> asteroidStack;
        for (const auto &a: asteroids) {
            collideAsteroid(a, asteroidStack);
        }
        return asteroidStack;  
    }
};
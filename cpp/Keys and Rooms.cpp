#include "common.h"

class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        stack<int> keys;
        unordered_set<int> visited_rooms;
        visited_rooms.insert(0);

        for (auto key: rooms[0]) {
            keys.push(key);
        }
        while (keys.size() > 0) {
            int current_key = keys.top();
            keys.pop();
            visited_rooms.insert(current_key);
            for (auto key: rooms[current_key]) {
                
                if (visited_rooms.count(key) == 0) {
                    keys.push(key);
                }
            }
        }
        return visited_rooms.size() == rooms.size();
    }
};
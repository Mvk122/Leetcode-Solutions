#include "common.h"
#include "queue"
#include <set>

struct Position {
    int x;
    int y;
    int steps_to_here;
};

class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        queue<Position> positions;
        positions.push({entrance[0], entrance[1], 0});

        vector<vector<int>> moves = {
            {1, 0},
            {0, 1},
            {-1, 0},
            {0, -1}
            };

        set<pair<int, int>> seen_moves;

        while (!positions.empty()) {
            Position current = positions.front();
            positions.pop();

            if (current.x == 0 || current.x == maze.size() -1 || current.y == 0 || current.y == maze.at(0).size()-1) {
                if (!(current.x == entrance[0] && current.y == entrance[1])) {
                    return current.steps_to_here;
                }
            }
            for (const auto& move: moves) {
                int new_x = current.x + move[0];
                int new_y = current.y + move[1];
                if (seen_moves.count({new_x, new_y}) == 0 && new_x >= 0 && new_x < maze.size() && new_y >=0 && new_y <maze.at(0).size()) {
                    if (maze[new_x][new_y] == '.') {
                        positions.push({new_x, new_y, current.steps_to_here+1});
                        seen_moves.insert({new_x, new_y});
                    }
                }
            }

        }   
        return -1;
    }
};
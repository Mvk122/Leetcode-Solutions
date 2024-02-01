#include "common.h"

// This solution does not work
class Solution {
public:

    int vertical_size(vector<vector<int>>& grid, int i, int j) {
        int total = 0;
        for (int k=i; k<i+3; k++) {
            total += grid[k][j];
        }
        return total;
    }
    int horizontal_size(vector<vector<int>>& grid, int i, int j) {
        int total = 0;
        for (int k=j; k<j+3; k++) {
            total += grid[i][k];
        }
        return total;
    }

    int diag_r_size(vector<vector<int>>& grid, int i, int j) {
        int total = 0;
        for (int k=0; k<3; k++) {
            total += grid[i+k][j+2-k];
        }
        return total;
    }

    int diag_l_size(vector<vector<int>>& grid, int i, int j) {
        int total = 0;
        for (int k=0; k<3; k++) {
            total += grid[i+k][j+k];
        }
        return total;
    }


bool isMagic(vector<vector<int>>& grid, int i, int j) { 
    if ((vertical_size(grid, i, j) == vertical_size(grid, i+1, j) && vertical_size(grid, i+1, j) == vertical_size(grid, i+2, j)) &&
        (horizontal_size(grid, i, j) == horizontal_size(grid, i, j+1) && horizontal_size(grid, i, j+1) == horizontal_size(grid, i, j+2)) &&
        (diag_l_size(grid, i, j) == diag_r_size(grid, i, j))) {
        return true;
    }
    return false;
}

    int numMagicSquaresInside(vector<vector<int>>& grid) {
    int count = 0;
    for (int i=0; i<=grid.size()-3; i++) {  // Change < to <=
        for (int j=0; j<=grid[0].size()-3; j++) {  // Change < to <=
            if (isMagic(grid, i, j)) {
                count++;
            }
        }
    }
    return count;
    }
};
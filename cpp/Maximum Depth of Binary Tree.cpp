#include "common.h"


class Solution {
public:
    void traverse(TreeNode* root, int current, int &deepest) {
        deepest = max(current,deepest);
        if (root->left) {
            traverse(root->left, current+1, deepest);
        }
        if (root->right) {
            traverse(root->right, current+1, deepest);
        }
    }
    int maxDepth(TreeNode* root) {
        int deepest = 1;
        if (root) {
            traverse(root, 1, deepest);
        } else {
            return 0;
        }
        return deepest;
     

    }
};
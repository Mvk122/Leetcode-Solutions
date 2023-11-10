from typing import Optional
import math
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, total):
        node_amount = 1
        value_sum = node.val

        if node.left:
            left_tree_nodes, left_tree_values = self.dfs(node.left, total)
            node_amount += left_tree_nodes
            value_sum += left_tree_values
        if node.right:
            left_tree_nodes, left_tree_values = self.dfs(node.right, total)
            node_amount += left_tree_nodes
            value_sum += left_tree_values

        if math.floor(value_sum / node_amount) == node.val:
            total[0] += 1
        
        return node_amount, value_sum

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        total = [0]
        self.dfs(root, total)
        return total[0]

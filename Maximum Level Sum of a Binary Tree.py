from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        highest = float('-inf')
        highest_level = 0
        current_level = 0
        queue = [root]

        while len(queue) > 0:
            current_level += 1
            current = queue.copy()
            queue.clear()

            layer_sum = 0
            for node in current:
                layer_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if layer_sum > highest:
                highest = layer_sum
                highest_level = current_level
            
        return highest_level
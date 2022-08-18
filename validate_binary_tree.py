class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isValidBST(self, root) -> bool:
        if root is None:
            return True
        if (root.left is not None) and root.left > root.val:
            return False
        if (root.right is not None) and root.right < root.val:
            return False
        if not self.isValidBST(root.left) or not self.isValidBST(root.right):
            return False
        return True
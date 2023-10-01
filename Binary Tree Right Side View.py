from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = [root]
        answer = []

        while len(queue) > 0:
            current = queue.copy()
            queue.clear()

            ret = 0
            for node in current:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                ret = node.val
            answer.append(ret)
        return answer



if __name__ == "__main__":
    a = TreeNode(5)
    a.right_amount = 4
    print(a.right_amount)
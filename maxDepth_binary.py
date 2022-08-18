def maxDepth(root):
    def maxDepth_f(root, current, max_depth):
        max_depth[0] = max(current, max_depth[0])
        if root is None:
            return
        if root.left:
            maxDepth_f(root.left, current+1, max_depth)
        if root.right:
            maxDepth_f(root.right, current+1, max_depth)
            
    if root is None:
        return 0
    max_depth = [0]
    maxDepth_f(root, 1, max_depth)
    return max_depth[0]
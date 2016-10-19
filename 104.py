# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.countDepth(root, 0)

    def countDepth(self, root, cnt):
        if not root:
            return cnt
        cnt += 1
        return max(self.countDepth(root.left, cnt), self.countDepth(root.right, cnt))


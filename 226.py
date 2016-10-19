# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        return root
    def invert(self, root):
        if root:
            tmp = root.right
            root.right = root.left
            root.left = tmp
            self.invert(root.right)
            self.invert(root.left)

            

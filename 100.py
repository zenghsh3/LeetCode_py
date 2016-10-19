# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_values = []
        self.visit(p, p_values)
        q_values = []
        self.visit(q, q_values)
        if p_values != q_values:
            return False
        else:
            return True
    
    def visit(self, root, values):
        if not root:
            values.append('null')
            return
        values.append(root.val)
        self.visit(root.left, values)
        self.visit(root.right, values)



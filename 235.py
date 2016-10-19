# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_fathers = []
        q_fathers = []
        tmp = root
        while tmp != p:
            p_fathers.append(tmp.val)
            if p.val > tmp.val:
                tmp = tmp.right
            else:
                tmp = tmp.left
        p_fathers.append(p.val)

        tmp = root
        while tmp != q:
            q_fathers.append(tmp.val)
            if q.val > tmp.val:
                tmp = tmp.right
            else:
                tmp = tmp.left
        q_fathers.append(q.val)

        ans = root.val
        for i in xrange(min(len(p_fathers), len(q_fathers))):
            if p_fathers[i] != q_fathers[i]:
                break
            ans = p_fathers[i]
        while root.val != ans:
            if ans > root.val:
                root = root.right
            else:
                root = root.left
        return root
         


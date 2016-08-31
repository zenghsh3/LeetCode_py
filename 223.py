class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        all = (C - A) * (D - B) + (G - E) * (H - F)
        l = max(A, E) 
        r = min(C, G)
        u = min(D, H)
        b = max(B, F)
        if r > l and u > b:
            return all - (r - l) * (u - b)
        else:
            return all

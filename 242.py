class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = {}
        for x in s:
            d1[x] = d1.get(x, 0)
            d1[x] += 1
        d2 = {}
        for x in t:
            d2[x] = d2.get(x, 0)
            d2[x] += 1
        if d1 != d2:
            return False
        else:
            return True


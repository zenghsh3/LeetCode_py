class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d1 = {}
        for x in s:
            d1[x] = d1.get(x, 0)
            d1[x] += 1
        d2 = {}
        for x in t:
            d2[x] = d2.get(x, 0)
            d2[x] += 1
        for x in d2:
            if x not in d1:
                return x
            if d2[x] != d1[x]:
                return x


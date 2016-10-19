class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for x in s:
            d[x] = d.get(x, 0)
            d[x] += 1
        for i in xrange(len(s)):
            if d[s[i]] == 1:
                return i 
        return -1

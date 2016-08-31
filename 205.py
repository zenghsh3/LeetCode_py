class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mapping = {}
        reverse = {}
        for i in xrange(len(s)):
            if s[i] not in mapping:
                if t[i] in reverse:
                    return False
                mapping[s[i]] = t[i]
                reverse[t[i]] = s[i]
            elif t[i] != mapping[s[i]]:
                return False
        return True


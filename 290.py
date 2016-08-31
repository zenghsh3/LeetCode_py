class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l = str.split(' ')
        if len(pattern) != len(l):
            return False
        mapping = {}
        reverse = {}
        for i in xrange(len(pattern)):
            if pattern[i] not in mapping:
                if l[i] in reverse:
                    return False
                mapping[pattern[i]] = l[i]
                reverse[l[i]] = pattern[i]
            elif l[i] != mapping[pattern[i]]:
                return False
        return True


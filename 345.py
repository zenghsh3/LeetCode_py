class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U'])
        s = list(s)
        if not s:
            return ''
        l = 0
        r = len(s) - 1
        while l != r:
            if s[l] in vowels and s[r] in vowels:
                tmp = s[r]
                s[r] = s[l]
                s[l] = tmp
                l += 1
                if l == r:
                    break
                r -= 1
            elif s[l] in vowels:
                r -= 1
            elif s[r] in vowels:
                l += 1
            else:
                l += 1
        return ''.join(s)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = self.preprocess(s)
        cnt = [0]
        center = 0
        for i in xrange(1, len(s) - 1):
            i_mirror = 2 * center - i
            center_r_bound = i_mirror + cnt[i_mirror]
            ans = 0
            if  center_r_bound > i:
                if cnt[i_mirror] <  i_mirror + cnt[i_mirror]:
                    ans = cnt[i_mirror]
                else:
                    ans = i_mirror + cnt[i_mirror] - i
                    center = i
            else:
                ans = 0
            while (s[i + ans + 1] == s[i - ans - 1]):
                ans += 1
            cnt.append(ans)
        max_index = 1
        max_num = 0
        for  i in xrange(1, len(s) - 1):
            if cnt[i] > max_num:
                max_num = cnt[i]
                max_index = i
        i = cnt[max_index]
        l = ''
        r = ''
        while i > 0:
            if s[max_index - i] != '#':
                l = l + s[max_index - i] 
            if s[max_index + i] != '#':
                r = s[max_index + i] + r
            i -= 1
        if s[max_index] != '#':
            l += s[max_index]
        return l + r

    def preprocess(self, s):
        ans = '^'
        for x in s:
            ans += '#'
            ans += x
        ans += '#'
        ans += '$'
        return ans

if __name__ == '__main__':
    solution = Solution()
    print solution.longestPalindrome('abba')


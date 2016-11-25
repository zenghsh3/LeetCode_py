#coding=utf8
# 最长无重复子串肯定在两个重复字符之间
# 用两个指针，当尾指针的字符在字典中时，头指针一直往后移，直到遇到和尾指针相同的字符，并从字典中删掉经过的字符

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = set([])
        head = 0
        tail = 0
        ans = 0
        while tail < len(s):
            if s[tail] in d:
                ans = max(ans, len(d))
                while (s[head] != s[tail]):
                    d.remove(s[head])
                    head += 1
                head += 1
            else:
                d.add(s[tail])
            tail += 1
        ans = max(ans, len(d))
        return ans



if __name__ == '__main__':
    s = 'abcdeafa'
    solution = Solution()
    ans = solution.lengthOfLongestSubstring(s)
    print ans

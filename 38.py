class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 1
        ans = '1'
        while (i < n):
            i += 1
            tmp = ''
            last = ans[0]
            count = 0
            for j in xrange(len(ans)):
                if ans[j] == last:
                    count += 1
                else:
                    tmp += str(count) + last
                    count = 1
                    last = ans[j]
            tmp += str(count) + last
            ans = tmp
        return ans

            
            

if __name__ == '__main__':
    solution = Solution()
    ans = solution.countAndSay(5)
    print ans

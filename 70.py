class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        bound = n / 2
        ans = 0
        m = 0
        while m <= bound:
            ans += self.combination(n, m)
            n -= 1
            m += 1
        return ans
            
    
    def combination(self, n, m):
        """
        select m from n
        """
        m = min(m, n - m)
        if m == 0:
            return 1
        ans = 1
        i = m
        while i > 0:
            ans *= n
            n -= 1
            i -= 1
        while m > 1:
            ans /= m
            m -= 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    print solution.climbStairs(9)

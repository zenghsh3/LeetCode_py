class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        ans = 0
        min_num = prices[0]
        for x in prices:
            if x < min_num:
                min_num = x
            else:
                ans = max(ans, x - min_num)
        return ans

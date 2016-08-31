class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        ans = [[1]]
        for i in xrange(1, numRows):
            ans.append([])
            ans[-1].append(1)
            if len(ans[-2]) > 1:
                for k in range(len(ans[-2]) - 1):
                    ans[-1].append(ans[-2][k] + ans[-2][k + 1])
            ans[-1].append(1)
        return ans

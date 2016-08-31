class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        max_money = []
        max_money.append(nums[0])
        max_money.append(max(nums[0], nums[1]))
        for i in xrange(2, len(nums)):
            max_money.append(max(max_money[i - 1], 
                    max_money[i - 2] + nums[i]))
        return max_money[-1]

if __name__ == '__main__':
    solution = Solution()
    print solution.rob([1, 3, 5, 3, 1])

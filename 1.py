class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i in xrange(len(nums)):
            key = target - nums[i]
            if key in num_dict:
                return [num_dict[key], i]
            num_dict[nums[i]] = i

if __name__ == '__main__':
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    ans = solution.twoSum(nums, target)
    print ans

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set([])
        i = 0
        while i < len(nums):
            if nums[i] in nums_set:
                del nums[i]
            else:
                nums_set.add(nums[i])
                i += 1
        return len(nums)

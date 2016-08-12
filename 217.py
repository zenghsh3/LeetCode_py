class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmp = set(nums)
        if len(tmp) < len(nums):
            return True
        else:
            return False

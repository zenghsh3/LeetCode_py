class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pos = {}
        for i in xrange(len(nums)):
            if nums[i] not in pos:
                pos[nums[i]] = i
            else:
                if i - pos[nums[i]] <= k:
                    return True
                pos[nums[i]] = i
        return False

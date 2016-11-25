class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = {}
        for x in nums:
            count[x] = count.get(x, 0)
            if count[x] >= 3:
                continue
            count[x] += 1
        print count
        uniq_nums = list(set(nums))
        uniq_nums.sort()
        ans = []
        for i in xrange(len(uniq_nums)):
            a = uniq_nums[i]
            done_set = set([])
            for j in xrange(i, len(uniq_nums)):
                b = uniq_nums[j]
                if b in done_set:
                    continue
                c = - a - b
                if c < a:
                    break
                count[a] = count.get(a, 0) 
                count[a] -= 1
                count[b] = count.get(b, 0) 
                count[b] -= 1
                count[c] = count.get(c, 0) 
                count[c] -= 1
                if count[a] >= 0 and count[b] >= 0 and count[c] >= 0:
                    ans.append([a, b, c])
                    done_set.add(c)
                count[a] += 1
                count[b] += 1
                count[c] += 1
        return ans

if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4];
    print solution.threeSum(nums)

        

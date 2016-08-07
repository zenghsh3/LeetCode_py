class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ans = a ^ b
        carries = a & b
        print ans
        print carries
        while carries:
            shift_carries = carries << 1
            carries = ans & shift_carries
            ans = ans ^ shift_carries
        return ans

if __name__ == '__main__':
    """ To-do
    - No consider negative num
    - python use 2's complement
    """
    solution = Solution()
    solution.getSum(-2, 2)

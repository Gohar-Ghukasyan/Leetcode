class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = set(nums)
        for element in unique_nums:
            count = nums.count(element)
            if count == 1:
                return element

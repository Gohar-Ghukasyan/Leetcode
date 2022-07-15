class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        n = ''
        for i in digits:
            n += str(i)
        n = int(n) + 1
        array = [int(i) for i in str(n)]
        return array

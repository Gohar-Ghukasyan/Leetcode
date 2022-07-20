class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        newStr = ""

        for char in s:
            if char.isalnum():
                newStr += char.lower()
        return newStr == newStr[::-1]

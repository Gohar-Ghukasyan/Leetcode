class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = False
        if (x < 0):
            neg = True
            x = -x

        Reversed_Number = 0
        while (x != 0):
            digit = x % 10
            Reversed_Number = (Reversed_Number * 10) + digit
            if (Reversed_Number >= 2147483647 or Reversed_Number <= -2147483647):
                return 0
            x = x // 10
        if neg:
            return -Reversed_Number
        return Reversed_Number
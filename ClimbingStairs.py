class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return (0)
        if n == 1:
            return (1)
        if n == 2:
            return (2)

        methods_per_steps = [1, 2]

        for i in range(2, n + 1):
            methods_per_steps.append(methods_per_steps[i - 1] + methods_per_steps[i - 2])
        return methods_per_steps[n - 1]

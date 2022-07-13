def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    if str(x)[:] == str(x)[::-1]:
        return True
    else:
        return False




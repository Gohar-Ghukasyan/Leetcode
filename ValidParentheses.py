def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    leftSymbols = []

    for i in s:

        if i in ['(', '{', '[']:
            leftSymbols.append(i)
        elif i == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
            leftSymbols.pop()
        elif i == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
            leftSymbols.pop()
        elif i == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
            leftSymbols.pop()
        else:
            return False

    return leftSymbols == []

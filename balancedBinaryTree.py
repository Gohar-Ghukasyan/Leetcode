# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None: return True

        def dfs(root):
            if root is None:
                return 0
            return max(dfs(root.left), dfs(root.right)) + 1

        return abs(dfs(root.left) - dfs(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

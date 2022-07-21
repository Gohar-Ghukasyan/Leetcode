# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = list()
        ans = list()

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            elif stack[-1].right:
                root = stack[-1].right
                stack[-1].right = None
            else:
                ans.append(stack.pop().val)

        return ans

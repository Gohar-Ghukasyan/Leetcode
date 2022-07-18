# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        result = []
        stack = []
        p = root
        while p or stack:
            # Save the nodes which have left child
            while p:
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                # Visit the middle node
                result.append(p.val)
                # Visit the right subtree
                p = p.right
        return result

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        if root is None:
            return False

        stack = [root]
        curr_list = []
        sum_vals = 0
        while len(stack) != 0:
            curr_root = stack.pop()
            sum_vals += curr_root.val
            curr_list.append(curr_root)
            if curr_root.left is None and curr_root.right is None:
                if sum_vals == targetSum:
                    return True
                while len(curr_list) > 0:
                    node = curr_list.pop()
                    if node.left is None and node.right is None:
                        sum_vals -= node.val
                        child_node = node
                    elif node.left == child_node and (node.right is None or not (node.right in stack)):
                        sum_vals -= node.val
                        child_node = node
                    elif node.right == child_node and (node.left is None or not (node.left in stack)):
                        sum_vals -= node.val
                        child_node = node
                    else:
                        curr_list.append(node)
                        break
            else:
                if curr_root.left is not None:
                    stack.append(curr_root.left)
                if curr_root.right is not None:
                    stack.append(curr_root.right)
        return False

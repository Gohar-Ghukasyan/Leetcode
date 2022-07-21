# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        st = []
        if root is not None:
            st.append(root)
            while len(st) != 0:
                tmp = st.pop()
                res.append(tmp.val)
                if tmp.right is not None:
                    st.append(tmp.right)
                if tmp.left is not None:
                    st.append(tmp.left)
        return res

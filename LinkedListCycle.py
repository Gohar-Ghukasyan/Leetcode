# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mp = set()
        while head is not None:
            if head in mp:
                return True
            mp.add(head)
            head = head.next
        return False

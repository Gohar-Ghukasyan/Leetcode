# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        current = head

        if head is None:
            return None

        while current.next:
            if current.val == current.next.val:
                next_element = current.next.next
                current.next = next_element
            else:
                current = current.next

        return head

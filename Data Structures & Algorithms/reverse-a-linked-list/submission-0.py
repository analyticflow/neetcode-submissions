# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Collect all values in a list, reverse the list, write back
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        values.reverse()

        curr = head
        for v in values:
            curr.val = v
            curr = curr.next

        return head
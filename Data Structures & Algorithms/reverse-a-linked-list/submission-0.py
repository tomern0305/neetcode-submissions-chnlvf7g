# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        if not head:
            return head
        while head.next:
            temp = head.next
            head.next = last
            last = head
            head = temp
        head.next = last
        return head
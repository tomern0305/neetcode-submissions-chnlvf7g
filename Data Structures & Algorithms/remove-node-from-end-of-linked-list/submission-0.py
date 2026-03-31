# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp = head
        lenght = 0

        while temp:
            lenght += 1
            temp = temp.next
        
        count = lenght - n
        if count == 0:
            return head.next
        
        temp = head
        for i in range(count -1):
            temp = temp.next

        temp.next = temp.next.next  # remove the nth node
        return head

        return head

       
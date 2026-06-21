# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr:
            l+=1
            curr = curr.next
        if l == 0 or l == 1:
            return 
        temp = head
        prev = None
        if l-n == 0:
            return head.next
        for i in range(l-n):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp.next = None
        return head

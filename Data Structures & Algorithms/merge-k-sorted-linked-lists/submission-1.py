# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        dummy = ListNode()
        curr = dummy
        l1 = lists[0]
        curr.next = l1
        for i in range(1, len(lists)):
            prev = dummy
            t1 = dummy.next
            t2 = lists[i]
            while t1 and t2:
                if t1.val < t2.val:
                    prev.next = t1
                    t1 = t1.next
                else:
                    prev.next = t2
                    t2 = t2.next
                prev = prev.next
            prev.next = t1 or t2
        return dummy.next

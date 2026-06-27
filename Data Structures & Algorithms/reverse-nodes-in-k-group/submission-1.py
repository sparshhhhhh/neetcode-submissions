class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_g_tail = dummy
        while True:
            kth = prev_g_tail
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            next_g_head = kth.next

            insert = next_g_head
            curr = prev_g_tail.next
            while curr != next_g_head:
                next_holder = curr.next
                curr.next = insert
                insert = curr
                curr = next_holder
            curr_g_tail = prev_g_tail.next
            prev_g_tail.next = kth
            prev_g_tail = curr_g_tail
        return dummy.next
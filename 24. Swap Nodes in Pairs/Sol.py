class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            ptr = current.next
            p1 = current.next.next

            ptr.next = p1.next
            p1.next = ptr
            current.next = p1

            current = current.next.next

        return dummy.next

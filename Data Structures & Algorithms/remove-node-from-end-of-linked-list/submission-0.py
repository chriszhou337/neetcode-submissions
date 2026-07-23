# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def determineSZ(head: Optional[ListNode]) -> int:
            size = 0

            curr = head
            while curr != None:
                size += 1
                curr = curr.next

            return size

        sz = determineSZ(head)
        remove = sz - n

        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        counter = 0
        while curr != None:
            if counter == remove:
                prev.next = curr.next
                break
            else:
                counter += 1
                curr = curr.next
                prev = prev.next

        return dummy.next
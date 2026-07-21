# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        while fast != None and fast.next != None:
            if fast == slow:
                return True

            fast = fast.next.next
            slow = slow.next

        return False
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode();
        ListNode originalStart = head;
        int carry = 0;

        while (l1 != null || l2 != null) {
            if (l1 == null) {
                int value = carry + l2.val;
                carry = 0;

                if (value >= 10) {
                    value = value - 10;
                    carry = 1;
                }

                head.next = new ListNode(value);
                l2 = l2.next;
                head = head.next;
                
            }
            else if (l2 == null) {
                int value = carry + l1.val;
                carry = 0;

                if (value >= 10) {
                    value = value - 10;
                    carry = 1;
                }

                head.next = new ListNode(value);
                l1 = l1.next;
                head = head.next;
            }
            else {
                int value = l1.val + l2.val + carry;
                carry = 0;

                if (value >= 10) {
                    value = value - 10;
                    carry = 1;
                }

                head.next = new ListNode(value);
                l1 = l1.next;
                l2 = l2.next;
                head = head.next;
            }
        }

        if (carry == 1) {
            head.next = new ListNode(1);
        }

        return originalStart.next;
    }
}

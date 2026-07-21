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
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode current = null;
        ListNode previous = null;
        ListNode next = null;

        while (head != null) {
            current = head;
            next = current.next;
            current.next = previous;
            previous = current;
            head = next;
        }
        
        return current;
    }
}

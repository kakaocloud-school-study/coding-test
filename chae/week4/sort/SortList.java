package codingTestStudy.week4.sort;

import java.util.List;

public class SortList {public static class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }

    public ListNode sortList(ListNode head) {
        if (head==null||head.next==null){
            return head;
        }
        sort(head, null);
        return head;
    }

    public void sort(ListNode head, ListNode end){
    if (head==null){
        return;
    }
    ListNode left = head;
    ListNode right = head;
    while (right!=end) {
        if (head.val > head.next.val) {
            int temp = head.val;
            head.val = head.next.val;
            head.next.val = temp;
        }
        right = head.next;
    }
    int num = left.val;
    left.val = head.val;
    head.val = num;
    sort(head.next, left);
    sort(head, right);
    }
}

package codingTestStudy.week4.sort;

import codingTestStudy.week4.sort.SortList.ListNode;

public class InsertionSortList {
    public ListNode insertionSortList(ListNode head) {
        ListNode parent = new ListNode();
        ListNode p = parent;

        // 다음 노드가 없을 때까지 순회
        while (head != null) {
            //다음 값이 정렬할 것보다 작으면 이동
            while (p.next != null && p.next.val < head.val)
                p = p.next;

            // 서로 위치를 교환하고 정렬을 해야 할 것은 다음 노드로 이동
            ListNode pNext = p.next;
            ListNode headNext = head.next;
            p.next = head;
            head.next = pNext;
            head = headNext;
            //다시 맨 앞으로 이동
            p = parent;
        }
        return parent.next;
    }
}

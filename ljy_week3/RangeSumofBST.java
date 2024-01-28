// Definition for a binary tree node.
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {
        // 교재 풀이
        // 예외 처리
        if (root == null) return 0;
        // 노드 값이 high 보다 크면 더 작아야하므로 왼쪽 노드 탐색
        if (root.val > high)
            return rangeSumBST(root.left, low, high);
        // 노드 값이 low 보다 작으면 더 커야하므로 오른쪽 노드 탐색
        if (root.val < low)
            return rangeSumBST(root.right, low, high);
        // 여기까지 도달했다면 노드 값이 low와 high 범위 내에 있으므로 모든 결과를 합산하여 리턴
        return root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high);
    }
}
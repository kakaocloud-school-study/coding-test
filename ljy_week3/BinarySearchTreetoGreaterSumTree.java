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
    int val = 0;
    public TreeNode bstToGst(TreeNode root) {
        // 교재 풀이
        if (root != null) {
            // 오른쪽 자식 노드부터 탐색
            bstToGst(root.right);
            // 누적된 값이 현재 노드값 추가
            val += root.val;
            // 현재 노드값을 지금까지 누적된 값으로 할당
            root.val = val;
            // 왼쪽 자식 노드 탐색
            bstToGst(root.left);
        }
        return root;
    }
}
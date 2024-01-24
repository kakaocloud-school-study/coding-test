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
    public int maxDepth(TreeNode root) {
        return getDepth(root);
    }

    private int getDepth(TreeNode node) {
        if (node == null) return 0; // node가 존재하지 않을 때 0을 반환
        if (node.left == null && node.right == null) { // 자식 노드가 없을 때 깊이 1을 반환
            return 1;
        }
        // 위 두 조건이 해당되지 않는 경우
        // 깊이는 왼쪽 자식과 오른쪽 자식 중 더 큰 깊이 + 1이다.
        return Math.max(getDepth(node.left), getDepth(node.right)) + 1;
    }
}
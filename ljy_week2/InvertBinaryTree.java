
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
    public TreeNode invertTree(TreeNode root) {
        invert(root);
        return root;
    }

    private void invert(TreeNode node) {
        // 노드가 없거나 자식이 없는 경우 반환
        if (node == null || node.left == null && node.right == null) return;

        // 양쪽 노드 각각 invert
        invert(node.left);
        invert(node.right);

        // 양쪽 노드 invert
        TreeNode temp = node.left;

        node.left = node.right;
        node.right = temp;
    }
}
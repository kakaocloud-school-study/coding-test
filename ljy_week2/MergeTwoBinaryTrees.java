
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
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        return mergeNode(root1, root2);
    }

    private TreeNode mergeNode(TreeNode node1, TreeNode node2) {
        // 두 노드가 존재하지 않을 때 null 반환
        if (node1 == null && node2 == null) return null;

        // 한 쪽이 없을 때 다른 한 쪽 반환
        if (node1 == null) return node2;
        if (node2 == null) return node1;

        // 둘 다 존재할 때 각각 merge후 새 TreeNode를 만들어 반환
        TreeNode left = mergeNode(node1.left, node2.left);
        TreeNode right = mergeNode(node1.right, node2.right);
        return new TreeNode(node1.val + node2.val, left, right);
    }
}
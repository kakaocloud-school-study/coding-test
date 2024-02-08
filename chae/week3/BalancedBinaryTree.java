public class BalancedBinaryTree {
    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) return 0;
        int result = 0;
        if (low <= root.val && root.val <= high)
            result = root.val;
        result += rangeSumBST(root.left, low, high);
        result += rangeSumBST(root.right, low, high);

        return result;
    }
}

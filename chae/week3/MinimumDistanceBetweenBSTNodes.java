
class MinimumDistanceBetweenBSTNodes {
        int bef = Integer.MIN_VALUE + 100000;
        int min = Integer.MAX_VALUE;

        public int minDiffInBST(TreeNode root) {
            if (root.left != null) minDiffInBST(root.left);

            min = Math.min(min, root.val - bef);
            bef = root.val;

            if (root.right != null) minDiffInBST(root.right);
            return min;
        }
    }
}

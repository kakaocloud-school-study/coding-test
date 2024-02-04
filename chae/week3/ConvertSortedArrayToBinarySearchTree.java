public class ConvertSortedArrayToBinarySearchTree {
    public TreeNode sort(int[] nums, int lo, int hi) {
        if (lo > hi) return null;
        int mid = lo + (hi - lo) / 2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = sort(nums, lo, mid - 1);
        node.right = sort(nums, mid + 1, hi);
        return node;
    }

    public TreeNode sortedArrayToBST(int[] nums) {
        if (nums.length == 0) return null;
        return sort(nums, 0, nums.length - 1);
    }
}

class BinaryTreeMaximum {
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

    int max=0;
    public int maxDepth(TreeNode root) {
        int count=0;
        dfs(root, count);
        return max;
    }

    public void dfs(TreeNode node, int count){
        if(node==null){
            if(count > max){
                max=count;
            }
            return;
        }

        dfs(node.left, count+1);
        dfs(node.right, count+1);
    }
}
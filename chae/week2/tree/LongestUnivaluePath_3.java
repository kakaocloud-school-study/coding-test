class Solution {
    int max=0;
    public  int longestUnivaluePath(TreeNode root) {
        if (root==null){
            return 0;
        }
        dfs(root);
        return max;
    }

    private int dfs(TreeNode node){
        if(node==null){
            return 0;
        }
        int val = 0;
        int left = dfs(node.left);
        int right = dfs(node.right);
        if(node.left!=null&&node.left.val == node.val){
            val= Math.max(val,left+1);
        }
        if(node.right!=null&&node.right.val == node.val){
            val= Math.max(val,right+1);
        }
        if(node.left!=null&&node.left.val == node.val&&node.right!=null&&node.right.val == node.val){
            max = Math.max(max,left+right+2);
        }
        max = Math.max(max, val);

        return val;
    }
}
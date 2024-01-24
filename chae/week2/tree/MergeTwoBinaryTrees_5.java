class Solution {
    public static TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        if (root2==null){
            return root1;
        } else if (root1==null) {
            return root2;
        }
        merge(root1, root2, root1, false);
        return root1;
    }

    public static void merge( TreeNode node, TreeNode node2, TreeNode root, boolean l){
        if(node2==null){
            return;
        }
        if (node == null){
            if (l) {
                node = new TreeNode(0);
                root.left = node;
            }else {
                node = new TreeNode(0);
                root.right = node;
            }
        }
        node.val = node.val+node2.val;
        merge(node.left, node2.left, node, true);
        merge(node.right, node2.right, node, false);
    }
}

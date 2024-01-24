class BinaryTreeMaximum {
    //TreeNode 객체
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
            //현재 누적 count가 max보다 큰가?
            if(count > max){
                max=count;
            }
            return;
        }

        //왼쪽 자식노드(count +1을 해서 최대 깊이를 구함)
        dfs(node.left, count+1);
        //오른쪽 자식노드
        dfs(node.right, count+1);
    }
}
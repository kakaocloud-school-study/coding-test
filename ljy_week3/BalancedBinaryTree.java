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
    public boolean isBalanced(TreeNode root) {
        // 예외 처리
        if (root == null) return true;
        // bfs를 할 큐 선언
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        getDepth(root);

        while(!q.isEmpty()) {
            TreeNode cur = q.poll();
            // 자식 둘의 깊이 차이가 1보다 클 경우 false 반환
            if (Math.abs(getDepth(cur.left) - getDepth(cur.right)) > 1) return false;

            if (cur.left != null) q.add(cur.left);
            if (cur.right != null) q.add(cur.right);

        }
        // 모두 다 돌았다면(문제가 없다면) true 반환
        return true;
    }

    // 노드 깊이를 구하는 함수
    private int getDepth(TreeNode node) {
        // 노드가 존재 하지 않을 경우 0
        if (node == null) return 0;
        // 노드의 자식이 존재하지 않을 경우 1
        if (node.left == null && node.right == null) return 1;

        // 한 쪽만 자식이 있을 경우 그 자식 + 1
        if (node.left == null) return getDepth(node.right) + 1;
        if (node.right == null) return getDepth(node.left) + 1;

        // 양 쪽 모두 있을 경우 최댓값 + 1
        return Math.max(getDepth(node.left), getDepth(node.right)) + 1;
    }
}
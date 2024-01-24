import java.util.*;
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
    public int diameterOfBinaryTree(TreeNode root) {
        // (루트를 포함한 길이, 왼쪽 노드의 길이, 오른쪽 노드의 길이) 저장할 리스트
        int ret = 0;

        // bfs를 할 큐 선언
        Queue<TreeNode> q = new LinkedList<>();
        // 루트 추가
        q.add(root);

        // 트리를 돌며 최대 rootPath를 찾는다.
        while (!q.isEmpty()) {
            TreeNode cur = q.poll();
            ret = Math.max(ret, getRootPath(cur));

            if (cur.left != null) q.add(cur.left);
            if (cur.right != null) q.add(cur.right);
        }

        return ret;
    }

    // 자식 노드만으로 이루어진 경로 찾기
    private int getChildPath(TreeNode node) {
        if (node == null) return 0;
        int leftPath = 0;
        int rightPath = 0;

        if (node.left != null) leftPath = getChildPath(node.left) + 1;
        if (node.right != null) rightPath = getChildPath(node.right) + 1;

        return Math.max(leftPath, rightPath);
    }

    // 루트를 포함한 경로 찾기
    private int getRootPath(TreeNode node) {
        if (node.left == null && node.right == null) return 0;
        if (node.left == null) return getChildPath(node.right) + 1;
        if (node.right == null) return getChildPath(node.left) + 1;
        return getChildPath(node.right) + getChildPath(node.left) + 2;
    }
}
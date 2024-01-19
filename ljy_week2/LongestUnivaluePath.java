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
    public int longestUnivaluePath(TreeNode root) {
        if (root == null) return 0;
        int ret = 0;

        // bfs로 큐를 이용하여 모든 노드에 접근
        Queue<TreeNode> q = new LinkedList<>();

        q.add(root);

        while(!q.isEmpty()) {
            TreeNode cur = q.poll();

            ret = Math.max(ret, getPathInRoot(cur));

            if (cur.left != null) q.add(cur.left);
            if (cur.right != null) q.add(cur.right);
        }

        return ret;
    }

    private int getPathInRoot(TreeNode node) {
        // 노드가 없거나 자식이 없는 경우 0 반환
        if (node == null || (node.left == null && node.right == null)) return 0;

        // 한 쪽 자식이 없을 때 다른 쪽 자식이 값이 같으면 root를 포함한 경로와 root를 포함하지 않은 경우 + 1 중 큰 값을 가져온다.
        // 값이 다르면 0 반환
        if (node.left == null) {
            if (node.val == node.right.val)
                return Math.max(getPathExRoot(node.right) + 1, getPathInRoot(node.right));
            else return 0;
        }

        if (node.right == null) {
            if (node.val == node.left.val)
                return Math.max(getPathExRoot(node.left) + 1, getPathInRoot(node.left));
            else return 0;
        }

        // 노드가 두 쪽 모두 같을 때 양 쪽의 root 제외 경로의 합 + 2
        if (node.val == node.left.val && node.val == node.right.val) {
            return getPathExRoot(node.left) + getPathExRoot(node.right) + 2;
        }

        // 한 쪽만 같을 때 역시 비교
        if (node.val == node.left.val) {
            return Math.max(getPathExRoot(node.left) + 1, getPathInRoot(node.left));
        }

        if (node.val == node.right.val) {
            return Math.max(getPathExRoot(node.right) + 1, getPathInRoot(node.right));
        }

        // 양 쪽 값이 모두 다른 경우 0 반환
        return 0;
    }

    private int getPathExRoot(TreeNode node) {
        // 노드가 없거나 자식 노드가 없을 때 0 반환
        if (node == null || (node.left == null && node.right == null)) return 0;

        // 한 쪽 노드가 없을 때 다른 한쪽의 root 제외 경로 + 1을 반환, 두 값이 다르면 0 반환.
        if (node.left == null) {
            if (node.val == node.right.val) return getPathExRoot(node.right) + 1;
            return 0;
        }
        if (node.right == null) {
            if (node.val == node.left.val) return getPathExRoot(node.left) + 1;
            return 0;
        }

        // 둘이 같으면 큰 쪽을 반환.
        if (node.val == node.left.val && node.val == node.right.val)
            return Math.max(getPathExRoot(node.left), getPathExRoot(node.right)) + 1;
        if (node.val == node.left.val) return getPathExRoot(node.left) + 1;
        if (node.val == node.right.val) return getPathExRoot(node.right) + 1;

        return 0;
    }
}
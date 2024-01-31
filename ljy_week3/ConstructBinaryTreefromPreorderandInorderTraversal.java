/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // 교재 풀이
        return dfs(0, 0, inorder.length - 1, preorder, inorder);
    }

    private TreeNode dfs(int preIndex, int inStart, int inEnd, int[] preorder, int[] inorder) {
        // 예외 처리
        if (preIndex > preorder.length - 1 || inStart > inEnd) return null;

        //  전위 순회 값이 중위 순회에서는 몇 번째 인덱스인지 추출
        int inIndex = 0;
        for (int i = inStart; i <= inEnd; i++) {
            if (inorder[i] == preorder[preIndex])  inIndex = i;
        }

        // 해당 인덱스는 중위 순회를 분할하는 노드로 지정
        TreeNode node = new TreeNode(inorder[inIndex]);
        // 전위 순회 다음 결과를 보도록 인덱스 + 1
        preIndex++;
        // 왼쪽 자식 노드부터 진행
        node.left = dfs(preIndex, inStart, inIndex - 1, preorder, inorder);
        node.right = dfs(preIndex + inIndex - inStart, inIndex + 1, inEnd, preorder, inorder);

        return node;
    }
}
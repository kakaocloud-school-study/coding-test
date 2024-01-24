class Solution {
    var max =0;
    fun diameterOfBinaryTree(root: TreeNode?): Int {
        //주어진 노드가 null이면 0
        if(root==null) return 0
        dfs(root)
        return max
    }

    fun dfs(node: TreeNode?):Int{
        if(node==null){
            return 0
        }
        var l = dfs(node.left)
        var r = dfs(node.right)
        //현재 자식 노드 간의 거리와 max값과 확인
        max = maxOf(max, l+r)
        //더 높은 자식 노드 리턴
        return 1 + maxOf(l, r)
    }
}
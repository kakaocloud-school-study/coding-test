class Solution {
    var max =0;
    fun diameterOfBinaryTree(root: TreeNode?): Int {
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
        max = maxOf(max, l+r)
        return 1 + maxOf(l, r)
    }
}
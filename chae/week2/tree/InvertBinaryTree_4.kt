class Solution {
    fun invertTree(root: TreeNode?): TreeNode? {
        dfs2(root)
        return root
    }

    fun dfs2(node: TreeNode?): TreeNode? {
        if(node==null){
            return node
        }

        val l = dfs2(node.left)
        val r = dfs2(node.right)
        node.left = r
        node.right = l
        return node
    }
}
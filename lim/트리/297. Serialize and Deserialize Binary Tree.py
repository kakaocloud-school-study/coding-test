'''
리스트 형태로 직렬화할 때 트리 노드 개수가 10^4 이므로 트리 높이가 10^4인 최악의 경우 엄청난 길이의 리스트를 만들어야 한다.
빈 가지를 압축할 수 있도록 해시맵 형태로 압축하는 것이 좋다.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        binary_tree_dict = dict()
        def dfs(node: TreeNode, idx):
            if node == None:
                return
            binary_tree_dict[idx] = node.val
            dfs(node.left, 2*idx+1)
            dfs(node.right, 2*idx+2)
        dfs(root, 0)

        serialized = ''
        for key in binary_tree_dict.keys():
            serialized += '{}:{},'.format(key, binary_tree_dict[key])
        return serialized[:-1]

    def deserialize(self, data):
        if data == '':
            return None
        
        binary_tree_dict = {int(e.split(':')[0]):int(e.split(':')[1]) for e in data.split(',')}

        def dfs(idx):
            if binary_tree_dict.get(idx) == None:
                return
            left = dfs(2*idx+1)
            right = dfs(2*idx+2) 
            node = TreeNode(binary_tree_dict[idx])
            node.left = left
            node.right = right      
            return node
        return dfs(0)

aaa = Codec().deserialize('0:1,1:2,2:3,5:4,6:5')
print(aaa)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
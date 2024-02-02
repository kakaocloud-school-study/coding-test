class Trie:

    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        word += ';'
        def _insert(node, word):
            if len(word) == 0:
                return
            if node.get(word[0]) == None: # 트라이에 없는 경우
                new_node = dict()
                node[word[0]] = new_node # 새 글자에 해당하는 노드 만들고 연결
                _insert(new_node, word[1:]) # 새 노드로 재귀 반복
            else:
                _insert(node[word[0]], word[1:]) # 이미 있는 노드로 재귀 반복
        _insert(self.root, word)

    def search(self, word: str) -> bool:
        word += ';'
        def _search(node, word):
            if len(word) == 0:
                return True
            if node.get(word[0]) == None: # 트라이에 없는 경우
                return False
            else:
                return _search(node[word[0]], word[1:]) # 재귀 반복
        return _search(self.root, word)

    def startsWith(self, prefix: str) -> bool:
        def _startsWith(node, prefix):
            if len(prefix) == 0:
                return True
            if node.get(prefix[0]) == None: # 트라이에 없는 경우
                return False
            else:
                return _startsWith(node[prefix[0]], prefix[1:]) # 재귀 반복
        return _startsWith(self.root, prefix)
        
trie = Trie()
trie.insert('apple')
trie.search('apple')
trie.startsWith('apple')


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
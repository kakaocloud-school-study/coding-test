from collections import defaultdict
from typing import List


class Trie:

    def __init__(self):
        self.root = dict()

    def insert(self, word: str, idx: int) -> None:
        word = word[::-1] + ';'
        def is_pal(word):
            return word == word[::-1]
        def _insert(node, word):
            if is_pal(word):
                if word == '':
                    node['id'] = idx
                if node.get('pal_ids') == None:
                    node['pal_ids'] = []
                node['pal_ids'].append(idx)
                return
            if node.get(word[0]) == None: # 트라이에 없는 경우
                new_node = dict()
                node[word[0]] = new_node # 새 글자에 해당하는 노드 만들고 연결
                _insert(new_node, word[1:]) # 새 노드로 재귀 반복
            else:
                _insert(node[word[0]], word[1:]) # 이미 있는 노드로 재귀 반복
        _insert(self.root, word)

    def search(self, word: str, idx: int) -> bool:
        word += ';'
        pairs = []
        def is_pal(word):
            return word == word[::-1]
        def _search(node, word):
            if len(word) == 0:
                if node.get('id'):
                    pairs.append((idx, node['id']))
                if node.get('pal_ids'):
                    for id in node['pal_ids']:
                        pairs.append((idx, id))
                return
            if is_pal(word) and node.get('id'):
                pairs.append((idx, node['id']))
            if node.get(word[0]) == None: # 트라이에 없는 경우
                return
            else:
                return _search(node[word[0]], word[1:]) # 재귀 반복
        _search(self.root, word)
        return pairs

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        answers = []
        trie = Trie()
        for i, word in enumerate(words):
            trie.insert(word, i)
        for i, word in enumerate(words):
            answers += trie.search(word, i)
        return answers
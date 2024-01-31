from collections import defaultdict, deque
import sys
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        node_2_degree = defaultdict(int)
        for edge in edges:
            src, dst = edge
            graph[src].add(dst)
            graph[dst].add(src)
            node_2_degree[src] += 1
            node_2_degree[dst] += 1
        
        while len(node_2_degree) > 2:
            leaf_nodes = []
            for node in node_2_degree:
                if node_2_degree[node] == 1:
                    leaf_nodes.append(node)
            for node in leaf_nodes:
                node_2_degree.pop(node)
                while len(graph[node]):
                    adj_node = graph[node].pop()
                    graph[adj_node].remove(node)
                    node_2_degree[adj_node] -= 1

        if n == 1:
            return [0]
        
        return node_2_degree.keys()

Solution().findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]])
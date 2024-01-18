from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        out_degree = [0] * numCourses
        graph = defaultdict(set)
        for prerequisite in prerequisites:
            post, pre = prerequisite
            graph[pre].add(post)
            out_degree[pre] += 1
            in_degree[post] += 1
        
        def pop_end_nodes(end_nodes):
            next_end_nodes = []
            for node in end_nodes:
                for next_node in graph[node]:
                    in_degree[next_node] -= 1
                    out_degree[node] -= 1
                    if in_degree[next_node] == 0:
                        next_end_nodes.append(next_node)
            return next_end_nodes
        
        end_nodes = []
        for node in range(numCourses):
            if in_degree[node] == 0:
                end_nodes.append(node)
        
        while len(end_nodes):
            end_nodes = pop_end_nodes(end_nodes)
        
        return sum(in_degree) == 0
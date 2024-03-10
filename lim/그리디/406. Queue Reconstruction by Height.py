'''
키가 크고 앞사람 카운트가 작은 사람 순으로 뽑고
앞사람 카운트의 인덱스로 insert하면 된다.

insert 할 때 Linked list로 풀이를 nlogn 최적화 가능할 듯
현재는 n^2 풀이
'''

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (x[0], -x[1]))
        answer = []
        while len(people):
            height, taller_count = people.pop()
            answer.insert(taller_count, (height, taller_count))
        return answer            
'''
visited 대신에 특정 num까지 도달하기 위한 연산수를 ops 배열에 저장하고 특정 경우가 기존 ops[num] 보다 적은 경우에만 갱신하는 식으로 가지치기
+1 연산후에 //2, //3 하는 편이 빠른 경우도 있으므로 ops 사이즈는 n이상이 될 수 있음
'''

from collections import deque
import sys

def sol(n):
    def bfs(n):
        ops = [sys.maxsize] * (2*n)
        ops[n] = 0
        dq = deque([(n, 0)])
        while len(dq):
            num, depth = dq.popleft()
            if num == 1:
                return depth

            if num % 2 == 0 and ops[num//2] > depth + 1:
                ops[num//2] = depth + 1
                dq.append((num//2, depth + 1))
            if num % 3 == 0 and ops[num//3] > depth + 1:
                ops[num//3] = depth + 1
                dq.append((num//3, depth + 1))
            if ops[num+1] > depth + 1:
                ops[num+1] = depth + 1
                dq.append((num+1, depth + 1))
            if ops[num-1] > depth + 1:
                ops[num-1] = depth + 1
                dq.append((num-1, depth + 1))
        return -1
    
    return bfs(n)

n = int(sys.stdin.readline())
print(sol(n))
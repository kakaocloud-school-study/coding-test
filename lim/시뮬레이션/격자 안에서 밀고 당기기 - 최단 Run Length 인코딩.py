from collections import deque
import sys


def sol(word):
    word_q = deque(word)
    answer = 0
    count = 1
    curr_ch = word_q.popleft()
    while len(word_q) and curr_ch == word_q[-1]:
        word_q.pop()
        count += 1
    while len(word_q):
        if curr_ch == word_q[0]:
            word_q.popleft()
            count += 1
        else:
            curr_ch = word_q.popleft()
            answer += 2
            count = 1
    if count >= 10:
        answer += 3
    else:
        answer += 2
    return answer
    

word = sys.stdin.readline().strip()
print(sol(word))
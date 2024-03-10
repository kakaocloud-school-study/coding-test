'''
스택 방식으로 한 글자씩 넣어간다
선택한 글자보다 작은 수가 스택 맨 위에 있으면 모두 뺀다
k 카운트가 남아있는 한 스택 맨위가 가장 큰 수 일 것이므로 스택 맨 위만 보면 된다
마지막으로 반환할 때 스택에 있는 숫자들을 조인하여 반환하되 남은 k 카운트만큼 뒤에서 자른 값을 반환한다
'''

def solution(number, k):
    answer = []
    for num in number:
        while len(answer) and k:
            if answer[-1] < num:
                answer.pop()
                k -= 1
            else:
                break
        answer.append(num)
    return ''.join(answer)[:len(number)-k]
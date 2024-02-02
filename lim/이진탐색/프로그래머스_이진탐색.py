'''
이진탐색 문제
'''

def solution(n, times):
    def check(time_limit):
        total_people = 0
        for cost in times:
            total_people += time_limit // cost
        return n <= total_people
    
    left, right = 1, max(times) * n # 최악의 경우인 10**81 (= 10**9 시간 걸리는 심사원 한 명에 10**9 명 대기하는 경우) 로 설정해도 무방하지만 입력값을 통해 상한을 최적화 가능
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
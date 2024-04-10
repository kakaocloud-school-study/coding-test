'''
k개 중 1개 n번 뽑기로 변수에 대입되는 수열 리스트를 구하고 이 수열들 각각의 결과를 구해 최대값을 찾는다
'''

import sys

def get_arrs(k, n):
    answer = []
    if n == 0:
        return [[]]
    subanswer = get_arrs(k, n-1)
    for num in range(1, k+1):
        for sublist in subanswer:
            answer.append([num] + sublist)
    return answer

def cal(vars, ops, arr):
    var_2_val = {var:arr[i] for i, var in enumerate(set(vars))}
    result = var_2_val[vars[0]]
    for i, op in enumerate(ops):
        var = vars[i+1]
        val = var_2_val[var]
        if op == '-':
            result -= val
        elif op == '+':
            result += val
        elif op == '*':
            result *= val
    return result

line = sys.stdin.readline().strip()
vars = [i for i in line if i not in '-+*']
ops = [i for i in line if i in '-+*']
arrs = get_arrs(4, len(set(vars)))
max_result = None
for arr in arrs:
    result = cal(vars, ops, arr)
    if max_result == None:
        max_result = result
    max_result = max(max_result, result)
print(max_result)
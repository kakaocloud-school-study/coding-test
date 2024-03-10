import sys

groups = sys.stdin.readline().strip().split(':')
answer = []

if groups[0] == '':
    groups = groups[1:]
if groups[-1] == '':
    groups = groups[:-1]
for group in groups:
    if group == '':
        for i in range(9 - len(groups)):
            answer.append('0000')
    else:
        answer.append('0'*(4 - len(group)) + group)
print(':'.join(answer))
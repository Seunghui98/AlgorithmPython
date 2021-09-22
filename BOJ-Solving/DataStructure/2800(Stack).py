# 괄호 제거 - BOJ 2800
# 스택 구현
from itertools import combinations

data = input()


stack = []
array = []
answer = []
for i in range(len(data)):
    if data[i] == '(':
        stack.append(i)
    elif data[i] == ')':
        num = stack.pop()
        array.append([i, num])

for i in range(1, len(array)+1):
    for com in list(combinations(array, i)):
        cut = []
        result = []
        for c in com:
            x, y = c
            cut.append(x)
            cut.append(y)
        for d in range(len(data)):
            if d in cut:
                continue
            else:
                result.append(data[d])
        answer.append(''.join(result))

answer = set(answer)
answer = list(answer)
for a in sorted(answer):
    print(a)

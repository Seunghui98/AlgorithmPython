# 쇠막대기 - BOJ 10799
# 스택
data = input()

stack = []
count = 0
for d in range(len(data)):
    if data[d] == '(':
        stack.append('(')
    else:
        if data[d-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            count += 1
            stack.pop()

print(count)

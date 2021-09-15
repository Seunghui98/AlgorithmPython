# 오리 - BOJ 12933
# 구현
duck = input()

visited = [False] * len(duck)
answer = 0


def solve(start):
    global answer
    quack = 'quack'
    j = 0
    first = True
    for i in range(start, len(duck)):
        if duck[i] == quack[j] and not visited[i]:
            visited[i] = True
            if duck[i] == 'k':
                if first:
                    answer += 1
                    first = False
                j = 0
                continue
            j += 1

if len(duck) % 5 != 0:
    print(-1)
else:
    for i in range(len(duck)):
        if duck[i] == 'q' and not visited[i]:
            solve(i)

    if not all(visited) or answer == 0:
        print(-1)
    else:
        print(answer)



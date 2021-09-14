# 지뢰 찾기 - BOJ 4396
# 구현
n = int(input())
graph1 = []
graph2 = []
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
answer1 = []
answer2 = []

for _ in range(n):
    array = input()
    graph1.append(array)

for _ in range(n):
    array = input()
    graph2.append(array)

what = False
for i in range(n):
    array = []
    array2 = []
    for j in range(n):
        if graph2[i][j] == 'x':
            if graph1[i][j] == '*':
                what = True
                array2.append('*')
            else:
                x, y = i, j
                cnt = 0
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                        continue
                    if graph1[nx][ny] == '*':
                        cnt += 1
                array.append(str(cnt))
                array2.append(str(cnt))
        else:
            array.append('.')
            if graph1[i][j] == '*':
                array2.append('*')
            else:
                array2.append('.')
    answer1.append(array)
    answer2.append(array2)

if what:
    for i in range(n):
        for j in range(n):
            print(answer2[i][j], end='')
        print()
else:
    for i in range(n):
        for j in range(n):
            print(answer1[i][j], end='')
        print()

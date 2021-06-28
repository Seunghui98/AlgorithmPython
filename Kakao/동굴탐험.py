# 카카오 2019 인턴 문제 
# 풀이법 (https://deok2kim.tistory.com/48)
from collections import deque
def solution(n, path, order):
    answer = True
    graph = {n:[] for n in range(n)}
    for x, y in path:
        graph[x].append(y)
        graph[y].append(x)

    precedeA = {}
    precedeB = {}

    for a, b in order:
        precedeA[a] = b
        precedeB[b] = a
        if b == 0:
            return False
        if a == 0:
            precedeA[0] = 0

    visited = [0] * n
    visited[0] = 1

    q = deque()
    q.append(0)

    while q:
        now = q.popleft()
        #알고보니 아직 못 가는 상태
        if now == precedeA.get(precedeB.get(now)):
            visited[now] = 2
        else:
            for x in graph[now]:
                if visited[x] == 0:
                    q.append(x)
                    visited[x] = 1

                    if precedeA.get(x): # 선행조건일 때
                        if visited[precedeA[x]] == 2: # 이 선행조건을 필요로 하는 친구가 준비상태이면
                            q.append(precedeA[x])
                            visited[precedeA[x]] = 1
                        precedeA[x] = 0

    for i in visited:
        if i == 0:
            return False
    return answer




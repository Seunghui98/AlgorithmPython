#BOJ 14889 - 스타트와 링크 => 백트래킹
import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [0 for _ in range(n)]
ans = int(1e9)

def dfs(idx, cnt):
    global ans
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += graph[i][j]

                elif not visited[i] and not visited[j]:
                    link += graph[i][j]
        ans = min(ans, abs(start-link))

    for i in range(idx, n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(i+1, cnt+1)
        visited[i] = 0


dfs(0, 0)
print(ans)

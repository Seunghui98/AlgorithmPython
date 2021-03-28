# BOJ - N과 M(1), 백트래킹
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [False] * n

def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, graph)))
        return

    for i in range(len(visited)):
        if not visited[i]:
            visited[i] = True
            graph.append(i+1)
            dfs(depth+1, n, m)
            visited[i] = False
            graph.pop()
            

dfs(0, n, m)

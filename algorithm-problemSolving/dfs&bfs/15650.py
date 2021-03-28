# BOJ 15650 N과 M(2) - 백트래킹
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * n


graph = []

def dfs(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, graph)))
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            graph.append(i+1)
            dfs(depth+1, i+1, n, m)
            visited[i] = False
            graph.pop()



dfs(0, 0, n, m)

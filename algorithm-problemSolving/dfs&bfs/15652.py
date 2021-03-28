# BOJ 15652번 - N과 M(4) - 백트래킹
import sys

input = sys.stdin.readline

n, m = map(int, input().split())



graph = []

def dfs(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, graph)))
        return
    for i in range(idx, n):
        graph.append(i+1)
        dfs(depth+1, i, n, m)
        graph.pop()



dfs(0, 0, n, m)

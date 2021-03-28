# BOJ - 15651 N과 M(3) 백트래킹(중복있는 순열)
import sys

input = sys.stdin.readline

n, m = map(int, input().split())



graph = []

def dfs(depth, n, m):
    if depth == m:
        print(' '.join(map(str, graph)))
        return
    for i in range(n):
        graph.append(i+1)
        dfs(depth+1, n, m)
        graph.pop()



dfs(0, n, m)

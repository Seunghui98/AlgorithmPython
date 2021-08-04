#BOJ 11725 - 트리의 부모찾기
#트리
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline


n = int(input())
parent = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent[1] = 1
def dfs(graph, v, parent):
    for i in graph[v]:
        if parent[i] == 0:
            parent[i] = v
            dfs(graph, i, parent)


dfs(graph, 1, parent)

for i in range(2, n+1):
    print(parent[i])

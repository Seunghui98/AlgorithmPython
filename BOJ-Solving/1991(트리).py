# 트리 순회 - BOJ 1991번
# 전위순회, 중위순회, 후위순회
# 재귀함수 이용
import sys

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]

pre_list = []
mid_list = []
post_list = []
for i in range(1, n+1):
    node, left, right = map(str, input().split())
    graph[i].append(node)
    graph[i].append(left)
    graph[i].append(right)


def tree(node):
    pre_list.append(graph[node][0])
    if graph[node][1] != '.':
        for i in range(1, n+1):
            if graph[i][0] == graph[node][1]:
                tree(i)

    mid_list.append(graph[node][0])
    if graph[node][2] != '.':
        for i in range(1, n+1):
            if graph[i][0] == graph[node][2]:
                tree(i)
    post_list.append(graph[node][0])


tree(1)
print(''.join(pre_list))
print(''.join(mid_list))
print(''.join(post_list))

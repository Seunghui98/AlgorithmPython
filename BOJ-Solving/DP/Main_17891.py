import sys
sys.setrecursionlimit(400000)

input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(n+1)]

lst = list(map(int, input().split()))

for i in range(len(lst)):
    graph[lst[i]].append(i + 2)


power = [0] + list(map(int, input().split()))
visited = [False for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]

def dfs(x):
    visited[x] = True
    # 만약 현재 부사수라면
    if x != 1:
        dp[x][0] += power[x]*power[x]
        dp[x][1] += power[x]*power[x]
    print(x)
    max_val1 = 0
    max_val2 = 0
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            if x != 1:
                max_val1 = max(max_val1, dp[i][1])
                max_val2 = max(max_val2, dp[i][0])

    dp[x][0] += max_val1
    dp[x][1] += max_val2



dfs(1)
print(dp)
print(max(dp[1][0], dp[1][1]))


# BOJ - 대기업 승범이네(17891번)
# Tree DP
import sys
sys.setrecursionlimit(400000)

input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(n+1)]
select = [0 for i in range(n+1)]
lst = list(map(int, input().split()))

for i in range(len(lst)):
    graph[lst[i]].append(i + 2)


power = [0] + list(map(int, input().split()))
visited = [False for _ in range(n+1)]
dp = [[-1, -1] for _ in range(n+1)]

def dfs(x, stat):
    max_sum = dp[x][stat]
    if max_sum != -1:
        return max_sum
    max_sum = 0

    # 현재 노드가 멘티 or 아무 것도 x
    if stat == 0:
        sum = 0
        for i in graph[x]:
            sum += max(dfs(i, 0), dfs(i, 1))
        max_sum = max(max_sum, sum)
    else: # 현재 멘토인 경우
        sum = 0
        for i in graph[x]:
            temp1 = dfs(i, 0)
            temp2 = dfs(i, 1)
            if(temp1 > temp2):
                sum += temp1
                select[i] = 0
            else:
                sum += temp2
                select[i] = 1
        for i in graph[x]:
            sum2 = sum - dfs(i, select[i])
            sum2 += (dfs(i, 0) + power[i] * power[x])
            max_sum = max(max_sum, sum2)
    dp[x][stat] = max_sum
    return max_sum



ans = max(dfs(1, 0), dfs(1, 1))


print(ans)






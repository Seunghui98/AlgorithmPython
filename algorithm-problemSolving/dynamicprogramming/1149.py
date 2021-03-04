# BOJ RGB 거리 1149번
n = int(input())


dp = [[0, 0, 0] for _ in range(n+1)]

for i in range(1, n+1):
  color = list(map(int, input().split()))
  
  if i == 1:
    dp[1] = color
  else:
    # 점화식을 통해 DP table
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + color[0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + color[1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + color[2]


print(min(dp[n]))

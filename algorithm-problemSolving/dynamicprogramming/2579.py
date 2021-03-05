# BOJ 계단 오르기 2579번
import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+3)]
array = [0 for _ in range(n+3)]
for k in range(1, n+1):
    array[k] = int(input())

dp[1] = array[1]
dp[2] = array[1] + array[2]
dp[3] = array[3] + max(array[1], array[2])

for i in range(4, n+1):
    dp[i] = array[i] + max(dp[i-3] + array[i-1], dp[i-2])

print(dp[n])

# 퇴사 - BOJ 14501
# DP
n = int(input())

t = []
p = []
dp = [0] * (n+1)

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(n-1, -1, -1):
    # i일에 상담을 하는 것이 퇴사 날짜 넘음
    if i + t[i] > n:
        dp[i] = dp[i+1]
    else:
        # i일에 상담을 하지 않는 경우와 상담을 하는 경우 중 비용이 큰 값으로 선택
        dp[i] = max(dp[i+t[i]]+p[i], dp[i+1])

print(dp[0])

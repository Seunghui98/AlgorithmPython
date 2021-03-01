n = int(input())

t = [] # 각 상담을 완료하는 데 걸리는 시간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n+1) # dp 테이블 초기화

max_value = 0

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# 리스트를 뒤에서 거꾸로 확인 ( 다이나믹 프로그래밍 - 탑다운 방식 )
for i in range(n-1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담 기간 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
        

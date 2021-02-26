# 피보나치 함수를 재귀 함수로 구현
def fibo(x):
  if x == 1 or x == 2:
    return 1
  return fibo(x-1) + fibo(x-2)

# 탑다운 다이나믹 프로그래밍
def fibo2(x):
  # 종료조건
  if x == 1 or x == 2:
    return 1
  # 이미 계산한 적 있는 문제라면 그대로 반환
  if d[x] != 0:
    return d[x]
  # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
  d[x] = fibo2(x-1) + fibo2(x-2)
  return d[x]


print(fibo(4))

# 다이나믹 프로그래밍 - 메모이제이션
d = [0] * 100


print(fibo2(99))

# 다이나믹 프로그래밍 - 보텀업 방식
d2 = [0] * 100

d2[1] = 1
d2[2] = 1
n = 99

for i in range(3, n+1):
  d2[i] = d2[i-1] + d2[i-2]

print(d2[n])

# 계수 정렬을 이용해서 푸는 방법
n = int(input())
array = [0] * 1000001

for i in input().split():
  array[i-1] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if array[i] == 1:
    print("yes", end=' ')
  else:
    print("no", end=' ')

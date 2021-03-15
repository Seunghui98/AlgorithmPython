n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 가장 작은 수

result = 0

while True:
	for i in range(k):	# 가장 큰 수 K번 먼저 더하기
    	if m == 0:
        	break
        result += first
        m -= 1	# 더할 때마다 1씩 빼기
    if m == 0:
    	break
    result += second
    m -= 1	# 더할 때마다 1씩 빼기


print(result)

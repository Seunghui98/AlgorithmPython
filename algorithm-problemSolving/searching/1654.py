# BOJ 랜선 자르기 1654번
k, n = map(int, input().split())
data = []

for _ in range(k):
    data.append(int(input()))

data.sort()
start = 1
end = data[-1]
result = 0
while (start <= end):
    c = 0
    mid =  (start + end) // 2
    for i in data:
        c += (i // mid)
    if c < n:
        end = mid -1
    elif c >= n:
        result = mid
        start = mid + 1

print(result)

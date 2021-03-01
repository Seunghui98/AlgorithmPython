# BOJ 나무 자르기 2805번
n, m = map(int, input().split())

array = list(map(int, input().split()))

array.sort()
start = 1
end = array[-1]
result = 0

while (start <= end):
    mid = (start + end) // 2
    c = 0
    for i in array:
        if mid < i:
            c += (i -mid)
    if c >= m:
        result = mid
        start = mid +1
    else:
        end = mid -1

print(result)

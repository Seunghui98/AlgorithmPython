# BOJ 수 찾기 1920번
n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
data = list(map(int, input().split()))

def binary_search(x, n):
    start = 0
    end =  n-1
    while (start <= end):
        mid = (start + end) // 2
        if array[mid] == x:
            return 1
        elif array[mid] < x:
            start = mid +1
        else:
            end = mid -1
    return 0

for i in data:
    print(binary_search(i, n))

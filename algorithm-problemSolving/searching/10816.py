# BOJ 숫자카드2 10816번
from bisect import bisect_left, bisect_right

n = int(input())
array = list(map(int, input().split()))
array.sort()

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

m = int(input())
data = list(map(int, input().split()))

for i in data:
    print(count_by_range(array, i, i), end=' ')

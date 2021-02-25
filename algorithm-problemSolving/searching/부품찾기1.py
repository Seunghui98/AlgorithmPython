# 이진 탐색으로 푸는 법
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return "yes"
    elif array[mid] > target:
      end = mid = 1
    else:
      start = mid + 1
  return "no"

n = int(input())
array = list(map(int, input().split()))

array.sort()
m = int(input())
data = list(map(int, input().split()))


for i in range(m):
  print(binary_search(array, data[i], 0, n-1),  end=' ')




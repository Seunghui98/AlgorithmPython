import heapq

#오름차순 힙 정렬(Heap Sort) - 최소힙
def heapsort1(iterable):
  h = []
  result = []

  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소들을 차례대로 꺼내 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))

  return result

# 내림차순 힙 정렬(Heap Sort) - 최대힙
def heapsort2(iterable):
  h = []
  result = []

  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value)
  # 힙에 삽입된 모든 원소들을 차례대로 꺼내 담기
  for i in range(len(h)):
    result.append(-heapq.heappop(h))

  return result

result = heapsort1([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

result = heapsort2([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

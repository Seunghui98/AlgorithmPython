# 풍선 터뜨리기 - BOJ 2346
# 데크
from collections import deque

n = int(input())
answer = []
queue = deque()
for i in range(1, n+1):
    queue.append(i)
data = list(map(int, input().split()))
queue2 = deque()
for i in data:
    queue2.append(i)


while len(queue):
    answer.append(queue.popleft())
    x = queue2.popleft()
    if x > 0:
        queue.rotate(-x+1)
        queue2.rotate(-x+1)
    else:
        queue.rotate(-x)
        queue2.rotate(-x)



for i in answer:
    print(i, end=' ')

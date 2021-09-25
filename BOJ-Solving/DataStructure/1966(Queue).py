# 프린터 큐 - BOJ 1966
# Queue
from collections import deque

for tc in range(int(input())):
    n, m = map(int, input().split())
    if n == 1:
        data = int(input())
        print(1)
    else:
        data = list(map(int, input().split()))
        queue = deque()
        for d in range(len(data)):
            queue.append((data[d], d))
        count = 1
        while queue:
            d, index = queue.popleft()
            max_value = 0
            for k in range(len(queue)):
                max_value = max(queue[k][0], max_value)
            if d >= max_value:
                if index == m:
                    what = True
                    print(count)
                    break
                else:
                    count += 1
            else:
                queue.append((d, index))

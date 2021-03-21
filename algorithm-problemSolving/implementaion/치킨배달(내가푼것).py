# 이코테 - 치킨배달(삼성전자 SW 역량테스트)
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = []
chicken = []
for i in range(n):
    data = list(map(int, input().split()))
    city.append(data)
    for j in range(0, n):
        if data[j] == 2:
            chicken.append([i, j])

best = list(combinations(chicken, m))


dist = 99999999
for k in best:
    sum = 0
    for i in range(0, n):
        for j in range(0, n):
            if city[i][j] == 1:
                min_dist = 9999999
                for c in range(0, m):
                    x, y = k[c]
                    min_dist = min(min_dist, abs(x-i)+abs(y-j))
                sum += (min_dist)
    dist = min(dist, sum)

print(dist)







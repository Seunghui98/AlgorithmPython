# 치킨배달 - BOJ 15686
# BFS(Combination) + 구현
n, m = map(int, input().split())
graph = []
chicken = []
home = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 2:
            chicken.append([i, j])
        elif data[j] == 1:
            home.append([i, j])

def combination(lst, num):
    result = []
    if num > len(lst):
        return result
    if num == 1:
        for i in lst:
            result.append([i])
    elif num > 1:
        for i in range(len(lst)-num+1):
            for temp in combination(lst[i+1:], num-1):
                result.append([lst[i]]+temp)
    return result

min_value = int(1e9)


def find_dis(c):
    global  min_value
    all_c = 0
    for h_x, h_y in home:
        min_c = 2*n+1
        for c_x, c_y in c:
            dist = (abs(h_x-c_x) + abs(h_y-c_y))
            min_c= min(min_c, dist)
        all_c += min_c
    min_value = min(min_value, all_c)


for c in combination(chicken, m):
    find_dis(c)

print(min_value)

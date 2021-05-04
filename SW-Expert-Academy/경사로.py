# BOJ 경사로 - 14890 
import sys
input = sys.stdin.readline

def check(li):
    sw = [False for _ in range(n)]
    for i in range(n-1):
        if li[i] == li[i+1]:
            continue
        if abs(li[i] - li[i+1]) > 1:
            return False


        if li[i] > li[i+1]:
            temp = li[i+1]
            for j in range(i+1, i+1+l):
                if 0<= j < n:
                    if li[j] != temp:
                        return False
                    if sw[j] == True:
                        return False
                    sw[j] = True
                else:
                    return False
        else:
            temp = li[i]
            for j in range(i, i-l, -1):
                if 0 <= j <n:
                    if li[j] != temp:
                        return False
                    if sw[j] == True:
                        return False
                    sw[j]= True
                else:
                    return False
    return True

n, l = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

count = 0
for i in graph:
    if check(i):
        count += 1

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(graph[j][i])
    if check(temp):
        count += 1

print(count)

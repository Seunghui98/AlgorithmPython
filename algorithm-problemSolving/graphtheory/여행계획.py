# 이코테 P.397 여행계획 - 서로소 집합 알고리즘 사용
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i


for i in range(1, v+1):
    array = list(map(int, input().split()))
    for j in range(1, v+1):
        if array[j-1] == 1:
            union_parent(parent, i, j)

travel = list(map(int, input().split()))

what = True
for k in range(1, e):
    if find_parent(parent, k) != find_parent(parent, k+1):
        what = False
        break

if what:
    print("YES")
else:
    print("NO")


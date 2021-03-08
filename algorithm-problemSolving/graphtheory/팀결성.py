# 이코테
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

for i in range(v+1):
  parent[i] = i

for i in range(e):
  what, a, b = map(int, input().split())
  if what == 1:
    if find_parent(parent, a) == find_parent(parent, b):
      print("YES")
    else:
      print("NO")
  else:
    union_parent(parent, a, b)



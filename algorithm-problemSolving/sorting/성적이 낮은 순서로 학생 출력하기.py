n = int(input())
array = []

for i in range(n):
  stu = input().split()
  array.append((stu[0], int(stu[1])))

array = sorted(array, key = lambda student: student[1])

for i in array:
  print(i[0], end=' ')

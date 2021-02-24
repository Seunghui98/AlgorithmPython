# BOJ 수 정렬하기3 10989번
import sys

n= int(input())
data = [0] * 10001

for _ in range(n):
  num = int(sys.stdin.readline())
  data[num] += 1
  
for i in range(10001):
  sys.stdout.write('%s\n' % i * data[i])

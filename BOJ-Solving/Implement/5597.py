# 과제 안 내신 분..? - BOJ 5597
# 
import sys


input = sys.stdin.readline

student = [0 for _ in range(31)]
for _ in range(28):
    n = int(input())
    student[n] = 1

for i in range(1, 31):
    if student[i] != 1:
        print(i)


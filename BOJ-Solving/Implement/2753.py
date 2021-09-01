# 윤년 - BOJ 2753
# 구현

import sys

input = sys.stdin.readline

n = int(input())

if(n%4 == 0):
    if(n%400==0 or n%100 != 0):
        print(1)
    else:
        print(0)
else:
    print(0)





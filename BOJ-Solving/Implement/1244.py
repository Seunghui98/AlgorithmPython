# 스위치 켜고 끄기 - BOJ 1244
# 단순 구현
import sys

input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))
l = len(data)
s = int(input())

def xy(number):
    start = number-1
    while start < l:
        if data[start] == 1:
            data[start] = 0
        else:
            data[start] = 1
        start += (number)



def xx(number):
    number -= 1
    left = number-1
    right = number+1
    if left < 0 or right > l-1 or data[left] != data[right]:
        if data[number] == 1:
            data[number] = 0
            return
        else:
            data[number] = 1
            return
    while left > -1 and right < l:
        if data[left] == data[right]:
            left -= 1
            right += 1
        else:
            break
    left += 1
    right -= 1

    for i in range(left, right+1):
        if data[i] == 1:
            data[i] = 0
        else:
            data[i] = 1


for _ in range(s):
    a, b = map(int, input().split())
    if a == 1:
        xy(b)
    else:
        xx(b)

sum_value = 0
for i in range(l):
    print(data[i], end=' ')
    sum_value += 1
    if sum_value >= 20:
        sum_value = 0
        print()

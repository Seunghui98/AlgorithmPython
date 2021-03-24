import sys

input = sys.stdin.readline

n = int(input())
room = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0

for i in range(len(room)):
    first = (room[i] - b)
    result += 1
    if first <= 0:
        continue
    elif (first % c == 0):
        result += (first // c)
    else:
        result += (first // c) + 1


print(result)

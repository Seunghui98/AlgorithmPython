# 원형 연결리스트 => 파이썬에서 구현으로 간단 해결
# BOJ -  요세푸스 문제
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
array = [i for i in range(1, n+1)]
answer = []

pointer = 0

for _ in range(n):
    pointer += (k-1)
    if pointer >= len(array):
        pointer = pointer % len(array)

    answer.append(str(array.pop(pointer)))


print("<", ", ".join(answer)[:], ">", sep="")

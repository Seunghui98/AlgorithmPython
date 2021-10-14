# 시험감독 - BOJ 13458
# 구현
n = int(input())
room = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
for r in room:
    r = r-b
    answer += 1
    if r > 0:
        if (r % c) > 0:
            answer += ((r // c) +1)
        else:
            answer += (r // c)

print(answer)

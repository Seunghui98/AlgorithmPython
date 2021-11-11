# 치킨치킨치킨 - BOJ 16439
# 조합
from itertools import combinations

n, m = map(int, input().split())

like = [list(map(int, input().split())) for _ in range(n)]
menu = [i for i in range(1, m+1)]
answer = 0
for combi in list(combinations(menu, 3)):
    a, b, c = combi[0], combi[1], combi[2]
    cnt = 0
    for i in range(n):
        score = [like[i][a-1], like[i][b-1], like[i][c-1]]
        cnt += max(score)
    answer = max(answer, cnt)

print(answer)

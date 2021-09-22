# 별 찍기 - 19, BOJ 10994
# 구현, 재귀함수
# (https://namhandong.tistory.com/104)
def solution(n, idx):
    if n == 1:
        map[idx][idx] = '*'
        return
    l = 4*n -3
    for i in range(idx, idx+l):
        # 위, 아래
        map[idx][i] = '*'
        map[idx+l-1][i] = '*'

        # 양, 옆
        map[i][idx] = '*'
        map[i][idx+l-1] = '*'
    return solution(n-1, idx+2)



n = int(input())
leng = 4*n -3
map = [[' '] * leng for _ in range(leng)]

solution(n, 0)

for i in range(leng):
    for j in range(leng):
        print(map[i][j], end='')
    print()


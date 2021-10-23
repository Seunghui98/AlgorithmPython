# SWEA 벌꿀채취
# DFS + 구현
T = int(input())
def solve2(idx, a, summ, result):
    if summ > c:
        return
    if idx == len(a) and summ <= c:
        alst.append(result)
        return
    solve2(idx+1, a, summ+a[idx], result+a[idx]**2)
    solve2(idx+1, a, summ, result)

def solve(c1, c2):
    arr1 = []
    arr2 = []
    money = 0
    global alst
    for j in range(m):
        arr1.append(board[c1[0]][c1[1]+j])
        arr2.append(board[c2[0]][c2[1]+j])
    if sum(arr1) > c:
        alst = []
        solve2(0, arr1, 0, 0)
        money += (max(alst))
    else:
        for a in arr1:
            money += (a*a)

    if sum(arr2) > c:
        alst = []
        solve2(0, arr2, 0, 0)
        money += (max(alst))
    else:
        for a in arr2:
            money += (a * a)
    return money

def combination(lst, num):
    result = []
    if num > len(lst):
        return result
    if num == 1:
        for l in lst:
            result.append([l])
    elif num > 1:
        for i in range(len(lst)-num+1):
            for temp in combination(lst[i+1:], num-1):
                result.append([lst[i]]+temp)
    return result

for test_case in range(1, T+1):
    n, m, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    c_lst = []
    for i in range(n):
        for j in range(n):
            if j+(m-1) > n-1:
                break
            c_lst.append([i, j])
    answer = -1

    for com in list(combination(c_lst, 2)):
        if com[0][0] == com[1][0] and abs(com[0][1]-com[1][1]) < m:
            continue
        answer = max(answer, solve(com[0], com[1]))
    print(f'#{test_case} {answer}')

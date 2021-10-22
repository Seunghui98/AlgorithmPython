# SWEA - 수영장
# DFS
T = int(input())

def dfs(m, cash):
    global min_money
    if m >= 13:
        min_money = min(min_money, cash)
        return
    else:
        dfs(m+1, cash+money[0]*month[m])
        dfs(m+1, cash+money[1])
        dfs(m+3, cash+money[2])

for test_case in range(1, T+1):
    money = list(map(int, input().split()))
    month = [0] + list(map(int, input().split()))
    min_money = money[3]
    dfs(1, 0)

    print(f'#{test_case} {min_money}')

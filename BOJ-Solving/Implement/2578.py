# 빙고 - BOJ 2578
# 구현, 반례(https://www.acmicpc.net/board/view/58812) 

bingo_dict = {}
bingo_visited = [[0] * 5 for _ in range(5)]

for i in range(5):
    data = list(map(int, input().split()))
    for j in range(5):
        bingo_dict[data[j]] = (i, j)

im = []

def check1(x, y):
    count = 0
    for p in range(5):
        if "h" + str(x) in im:
            break
        if bingo_visited[x][p] == 1:
            count += 1
        if count == 5:
            im.append("h" + str(x))
            return True
    return False
def check2(x, y):
    count = 0
    for p in range(5):
        if "v" + str(y) in im:
            break
        if bingo_visited[p][y] == 1:
            count += 1
        if count == 5:
            im.append("v" + str(y))
            return True
    return False
def check3(x, y):
    count = 0
    for p in range(5):
        if "c1" in im:
            break
        if bingo_visited[p][p] == 1:
            count += 1
        if count == 5:
            im.append("c1")
            return True
    return False
def check4(x, y):
    count = 0
    for p in range(5):
        if "c2" in im:
            break
        if bingo_visited[p][4 - p] == 1:
            count += 1
        if count == 5:
            im.append("c2")
            return True
    return False


cnt1 = 0
cnt2 = 0
what = False
for i in range(5):
    array = list(map(int, input().split()))
    for j in array:
        cnt1 += 1
        x, y = bingo_dict[j]
        bingo_visited[x][y] = 1
        if check1(x, y):
            cnt2 += 1
            if cnt2 == 3:
                what = True
                break
        if check2(x, y):
            cnt2 += 1
            if cnt2 == 3:
                what = True
                break
        if check3(x, y):
            cnt2 += 1
            if cnt2 == 3:
                what = True
                break
        if check4(x, y):
            cnt2 += 1
            if cnt2 == 3:
                what = True
                break
    if what:
        print(cnt1)
        break

# 이차원 배열과 연산 - BOJ 17140
# 구현 + dict
arr = [[0]*101 for _ in range(101)]

r, c, k = map(int, input().split())
m_r, m_c = 3, 3
for i in range(1, 4):
    data = map(int, input().split())
    arr[i][1:4] = data

count = 0

def cal_r():
    global m_r, m_c
    r, c = m_r, m_c
    r_m_c = -1
    for i in range(1, r+1):
        data = arr[i][1:c+1]
        dict = {data[j]:data.count(data[j]) for j in range(len(data))}
        if 0 in dict.keys():
            dict.pop(0)
        tp = list(dict.items())
        tp.sort(key=lambda x:(x[1], x[0]))
        if len(tp) > 50:
            l = 50
        else:
            l = len(tp)

        r_m_c = max(r_m_c, l * 2)
        temp = []
        for t in range(l):
            a, b = tp[t]
            temp.append(a)
            temp.append(b)
        arr[i][1:l * 2] = temp
        for t in range(l*2+1, 101):
            arr[i][t] = 0
    m_c = r_m_c


def cal_c():
    global m_r, m_c
    r, c = m_r, m_c
    r_m_r = -1
    for i in range(1, c + 1):
        data = []
        for j in range(1, r+1):
            data.append(arr[j][i])
        dict = {data[j]: data.count(data[j]) for j in range(len(data))}
        if 0 in dict.keys():
            dict.pop(0)
        tp = list(dict.items())
        tp.sort(key=lambda x: (x[1], x[0]))
        if len(tp) > 50:
            l = 50
        else:
            l = len(tp)
        r_m_r = max(r_m_r, l * 2)
        temp = []
        for t in range(l):
            a, b = tp[t]
            temp.append(a)
            temp.append(b)
        for t in range(len(temp)):
            arr[t+1][i] = temp[t]
        for t in range(2*l+1, 101):
            arr[t][i] = 0
    m_r = r_m_r

while True:
    if count > 100:
        print(-1)
        break
    if arr[r][c] == k:
        print(count)
        break

    if m_r >= m_c:
        cal_r()
        count += 1
    else:
        cal_c()
        count += 1

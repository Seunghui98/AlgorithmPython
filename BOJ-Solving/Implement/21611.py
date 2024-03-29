# 마법사 상어와 블리자드 - BOJ 21611
# 구현 
# 참조 (https://imksh.com/64)
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
field = [list(map(int,input().strip().split())) for _ in range(N)]
skills = [list(map(int,input().strip().split())) for _ in range(M)]


direction = [[0, 0], [0, -1], [0, 1], [-1, 0], [1, 0]] # 상, 하, 좌, 우
broken_marble = [0, 0, 0] # 파괴한 구슬의 수
indexing = {}

def init(): # 각 필드에 번호와 좌표 매칭
    x = (N+1) // 2 -1 # 필드 중심
    y = (N+1) // 2 -1
    index = 1
    turn = 1 # 현재 방향
    depth = 1
    # 서 - 남 - 동 - 북 (3, 2, 4, 1)
    tmpdir = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    tmpfield = [[0] * N for _ in range(N)]
    cnt = 0 # 같은 방향으로 이동한 횟수
    while x > -1 and y > -1:
        indexing[index] = [x, y] # 번호에 좌표를 넣음
        tmpfield[y][x] = index
        x += tmpdir[turn][0]
        y += tmpdir[turn][1]
        cnt += 1
        index += 1
        if cnt == depth: # 깊이와 동일하게 움직이면
            if turn in [0, 2]:
                depth += 1 # 남, 북일 때 depth 증가
            turn = (turn + 1) % 4 #방향 전환
            cnt = 0

def changeMarble(): # 구슬의 변화
    newfield = [[0] * N for _ in range(N)]
    index = 2
    start = 2
    end = 3
    same = 1
    # 그룹에 대한 구슬 정의 -> 구슬의 갯수 / 구슬의 번호
    while start < N*N and end <= N*N:
        sx, sy = indexing[start]
        ex, ey = indexing[end]
        if field[sy][sx] == field[ey][ex]: # 구슬이 같으면
            same += 1
            end += 1
        else: # 구슬이 달라졌을 때
            ix, iy = indexing[index]
            newfield[iy][ix] = same #구슬 갯수
            ix, iy = indexing[index+1]
            newfield[iy][ix] = field[sy][sx] # 구슬 번호
            index += 2
            same = 1
            start = end
            end = start + 1
        if index > N*N:
            break
    for i in range(N):
        for j in range(N):
            field[i][j] = newfield[i][j]

# 연속하는 구슬이 4개 이상일 때 파괴
def bombMarble(): # 구슬 파괴
    result = False
    start = 2
    end = 3
    same = 1 # 같은 구슬 수 카운팅
    while start < N*N and end <= N*N:
        sx, sy = indexing[start]
        ex, ey = indexing[end]
        if field[sy][sx] == field[ey][ex]: # 구슬 같으면 ?
            same += 1
            end += 1
        else: # 구슬 달라졌을 때
            if same >= 4: # 동일 구슬 4개 이상은 폭파 대상
                result = True
                # start ~ end -1 까지 폭파
                for i in range(start, end):
                    bx, by = indexing[i]
                    broken_marble[field[by][bx]-1] += 1 # 폭파되는 구슬 카운팅
                    field[by][bx] = 0 # 폭파
            same = 1
            start = end
            end = start + 1
    return result

def moveMarble(): #구슬의 이동
    start = 2 # 시작 인덱스 2
    end = 3
    while start < N*N and end <= N*N:
        while start < N*N: # 비어있는 필드 찾기
            sx, sy = indexing[start]
            if not field[sy][sx]: # 비어있다면
                break
            start += 1
        else: # 더이상 빈 칸이 없다면
            return
        if end <= start:
            end = start + 1

        while end <= N*N:
            ex, ey = indexing[end]
            if field[ey][ex]: # 구슬이 있다면
                break
            end += 1
        else: return#더이상 당길 구슬이 없다면
        field[sy][sx] = field[ey][ex]
        field[ey][ex] = 0

def blizzard(d, s): # 상어의 블리자드
    cx = (N+1) // 2-1
    cy = (N+1) // 2-1
    for i in range(1, s+1):
        nx = cx + direction[d][0]*i
        ny = cy + direction[d][1]*i
        if field[ny][nx]:
            # broken_marble[field[ny][nx]-1]+=1 블리자드로 파괴된 구슬도 합산되는 가?
            field[ny][nx] = 0

def testPrint():
    for i in range(N):
        for j in range(N):
            print(field[i][j], end=' ')
        print()

init()
for skill in skills:
    d, s = skill
    blizzard(d, s)
    moveMarble()
    while bombMarble():
        moveMarble()
    changeMarble()

print(broken_marble[0]+broken_marble[1]*2+broken_marble[2]*3)

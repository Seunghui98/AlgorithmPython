# 카카오 2020 인턴 경주로 건설 - 프로그래머스
from collections import deque

def solution(board):
    answer = 999999
    q = deque()
    q.append((0, 0, 4, 0))
    n = len(board)
    visited = {
        (0, 0, 1) : 0,
        (0, 0, 3) : 0,
    }

    #상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, d, c = q.popleft()

        # 마지막위치에 도달했을 경우
        if x == n-1 and y == n-1:
            answer = min(answer, c)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                cost = c
                if d == 4: # 맨처음 도로
                    cost += 100
                elif d <= 1 and i <= 1: # 바라보는 방향과 진행상황 같음(상, 하)
                    cost += 100
                elif d >= 2 and i >= 2: # 바라보는 방향과 진행상황 같음(좌, 우)
                    cost += 100
                else: # 바라보는 방향과 진행상황 다름
                    cost += 500 + 100

                # 방문한 적 없거나, 방문했어도 기존의 비용보다 지금온 경로의 비용이 더 적은 경우
                if not visited.get((nx, ny, i)) or visited[(nx, ny, i)] > cost:
                    visited[(nx, ny, i)] = cost # 비용을 추가하거나 갱신
                    q.append((nx, ny, i, cost)) # 다음 출발지 q에 삽입

    return answer


#  2021 카카오 채용연계형 인턴십 (프로그래머스)
# BFS 사용
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def solution(places):
    answer = []
    person = []
    for p in places:
        person_xy = []
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    person_xy.append([i, j])
        if bfs(p, person_xy):
            answer.append(1)
        else:
            answer.append(0)

    return answer


def bfs(graph, ps):

    for k in ps:
        visited = [[False, False, False, False, False] for _ in range(5)]
        q = deque()
        visited[k[0]][k[1]] = True
        q.append((k[0], k[1], 1))
        while q:
            x, y, dis = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                    continue
                if graph[nx][ny] == 'X':
                    continue
                else:
                    if graph[nx][ny] == 'P':

                        if dis <= 2 and (visited[nx][ny] == False):

                            return False

                    if visited[nx][ny] == False:
                            visited[nx][ny] = True
                            q.append([nx, ny, dis+1])
    return True



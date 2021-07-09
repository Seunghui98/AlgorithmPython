# 2019 카카오 개발자 겨울 인턴십 문제 (프로그래머스)
# 스택
def solution(board, moves):
    answer = 0
    n = len(board[0])
    board_stack = [[] for i in range(n+1)]
    bucket = []

    cnt = 0

    for i in board[::-1]:
        for j in range(n):
            if i[j] == 0:
                continue
            else:
                board_stack[j+1].append(i[j])

    for i in moves:
        if len(board_stack[i]) == 0:
            continue
        else:
            new = board_stack[i].pop(-1)
            if len(bucket) == 0:
                bucket.append(new)
            else:
                last = bucket.pop(-1)
                if last == new:
                    cnt += 2
                else:
                    bucket.append(last)
                    bucket.append(new)

    answer = cnt
    return answer

# 카카오2019 KAKAO BLIND RECRUITMENT 오픈채팅방 - 프로그래머스
import re


def solution(record):
    answer = []
    orders = []
    name = {}
    for i in record:
        open = re.split(' ', i)
        if open[0] == 'Enter':
            orders.append([open[1], 'Enter'])
            name[open[1]] = open[2]
        elif open[0] == 'Leave':
            orders.append([open[1], 'Leave'])
        elif open[0] == 'Change':
            name[open[1]] = open[2]

    for i in orders:
        if i[1] == 'Enter':
            str = name.get(i[0]) + "님이 들어왔습니다."
        else:
            str = name.get(i[0]) + "님이 나갔습니다."
        answer.append(str)

    return answer

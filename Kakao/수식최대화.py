# 카카오 인턴 2020 - 수식 최대화
from itertools import permutations
import copy


def solution(expression):
    num = ''
    count = 0
    cal = []
    oper = []
    for i in expression:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            num += i
            count += 1
        elif i in ['+', '-', '*']:
            cal.append(int(num))
            num = ''
            oper.append(i)
            cal.append(i)
            count += 1

        if count == len(expression):
            cal.append(int(num))

    oper = list(set(oper))
    oper_per = list(permutations(oper, len(oper)))
    max_sum = 0
    for i in oper_per:
        cal_copy = copy.copy(cal)
        print(i)
        for k in i:
            find_index = list(filter(lambda x: cal_copy[x] == k, range(len(cal_copy))))
            for _ in range(len(find_index)):
                j = cal_copy.index(k)
                result = 0
                if cal_copy[j] == '+':
                    result = cal_copy[j - 1] + cal_copy[j + 1]
                elif cal_copy[j] == '*':
                    result = cal_copy[j - 1] * cal_copy[j + 1]
                else:
                    result = cal_copy[j - 1] - cal_copy[j + 1]

                cal_copy[j - 1] = result
                del cal_copy[j]
                del cal_copy[j]
        print(abs(cal_copy[0]))
        max_sum = min(max_sum, abs(cal_copy[0]))

    answer = max_sum
    return answer

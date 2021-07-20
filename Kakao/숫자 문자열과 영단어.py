# 2021 카카오 채용연계형 인턴십 (프로그래머스)
# 문자열 처리

number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def solution(s):
    answer = ''
    word = ''
    for i in s:
        if i.isdigit():
            answer += i
            continue
        else:
            word += i

            if word in number:
                answer += str(number.index(word))
                word = ''

    answer = int(answer)

    return answer

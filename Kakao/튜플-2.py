# 2019 카카오 개발자 겨울 인턴십 문제 (프로그래머스)

def solution(S):
    S = S[2:-2].split("},{")
    numArr = []
    for i in range(len(S)):
        s = S[i].split(",")
        numArr.append(set(s))

    numArr.sort(key=lambda x: len(x))

    ans = set()
    res = []
    for a in numArr:
        tmp = a - ans
        res.append(list(tmp)[0])
        ans = ans | tmp

    res = [int(i) for i in res]
    return res

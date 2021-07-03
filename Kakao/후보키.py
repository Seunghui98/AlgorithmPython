# 카카오 2019 KAKAO BLIND RECRUITMENT (프로그래머스) - 후보키
from itertools import combinations
def solution(relation):
    answer = 0
    # 모든 컬럼의 조합 리스트
    all = list()

    # 유일성을 만족하는 조합 리스트
    uniqueIndex = []

    col_n = len(relation[0])
    row_n = len(relation)

    # 모든 컬럼의 조합 구하기 (set 형태)
    for i in range(1, col_n+1):
        #append는 런타임에러 -> append와 extend비교
        all.extend([set(k) for k in combinations([j for j in range(col_n)], i)])

    #유일성 검증
    for comb in all:
        # set에 추가하여 사이즈 비교로 검증
        vaildSet = set()
        # 조합에 해당하는 로우를 하나의 str로 합쳐서 set에 넣음
        for row in range(row_n):
            temp = ''
            for col in comb:
                temp += relation[row][col]
            vaildSet.add(temp)

        #유일성 확인하여 리스트에 추가
        if len(vaildSet) == row_n:
            uniqueIndex.append(comb)

    # 최소성 검증
    # 삭제대상 Set ( 최소성 위배 )
    delSet = set()
    # 부분집합 여부 확인
    for stdMinElem in uniqueIndex:
        for idx, compMinElem in enumerate(uniqueIndex):
            # 부분집합이면서 자기 자신이 아니라 상위집합을 삭제 대상에 추가
            # issubset()은 부분집합(subset)인가 확인하는 메소드
            if stdMinElem.issubset(compMinElem) and stdMinElem != compMinElem:
                delSet.add(uniqueIndex.index(compMinElem))
    # 답 = 유일성 - 최소성 위배
    answer = len(uniqueIndex) - len(delSet)
    return answer

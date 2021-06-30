# 보석쇼핑 - 카카오 2020 인턴십 문제 프로그래머스
# 투포인트 사용
def solution(gems):
    gemdict = {}
    answer = []
    min_len = len(gems) + 1
    start = 0
    end = 0
    n = len(set(gems))
    
    
    while end < len(gems):
        # 새로운 종류 추가
        if gems[end] not in gemdict:
            gemdict[gems[end]] = 1
        else:
            gemdict[gems[end]] += 1
        
        end += 1
        
        # 모든 종류가 딕셔너리에 있는 경우
        if len(gemdict) == n:
            while start < end:
                if gemdict[gems[start]] > 1:
                    gemdict[gems[start]] -= 1
                    start += 1
                elif min_len > end - start: # 기존의 구간 최단거리보다 현재의 구간거리가 더 짧다면
                    min_len = end - start
                    answer = [start+1, end] # 최단거리로 부터 answer 갱신
                else:
                    break
    
    return answer
                    

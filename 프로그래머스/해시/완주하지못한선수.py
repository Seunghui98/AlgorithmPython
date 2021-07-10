# 해시 
# 프로그래머스 레벨 1 - 완주하지 못한 선수
def solution(participant, completion):
    answer = ''
    part_dict = {}
    for i in participant:
        if i not in part_dict:
            part_dict[i] = 1
        else:
            part_dict[i] += 1
    
    for i in completion:
        part_dict[i] -= 1
    
    for key, value in part_dict.items():
        if value > 0:
            answer = key
    return answer

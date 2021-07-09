# 2019 카카오 개발자 겨울 인턴십 문제 (프로그래머스)
# 정규표현식, 딕셔너리
import re

def solution(s):
    answer = []
    result_dict = {}
    new_s = s[1:-1]
    new_s = re.split(r'[,:{}]', new_s)
    
    for i in new_s:
        if i == '':
            continue
        else:
            if i not in result_dict:
                result_dict[i] = 1
            else:
                result_dict[i] += 1
    result = sorted(result_dict.items(), key=lambda x: x[1], reverse=True)
    
    for i in result:
        answer.append(int(i[0]))
        
    
   
    return answer

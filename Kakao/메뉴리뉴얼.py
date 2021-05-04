# 프로그래머스 - 2021 카카오 메뉴리뉴얼
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for length in course:
        order_list = []
        for order in orders:
            for combi in combinations(order, length):
                order_list.append(''.join(sorted(combi)))
        
        if order_list:
            order_list = Counter(order_list).most_common()
            
            for word, cnt in order_list:
                if cnt > 1 and cnt == order_list[0][1]:
                    answer.append(word)
                else:
                    break
        
        answer.sort()
    return answer

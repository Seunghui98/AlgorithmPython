# 카카오 2020 인턴 - 수식최대화(간편 코드)
import re
from itertools import permutations

def solution(expression):
    op = [x for x in ['+', '*', '-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)', expression)
    
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1] + _ex[tmp] + _ex[tmp+1]))
                _ex = _ex[:tmp] + _ex[tmp+2:]
        
        a.append(_ex[-1])
    
    return max(abs(int(x)) for x in a)

# 2020 카카오 인턴 - 키패드 누르기
def trans(num):
    x_y = [[3, 1],[0,0],[0,1], [0,2],[1,0], [1,1], [1, 2], [2,0], [2, 1], [2, 2]]
    return x_y[num]

def solution(numbers, hand):
    answer = ''
    l_x, l_y = 3, 0
    r_x, r_y = 3, 2
    l_dis = 0
    r_dis = 0
    
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            l_x, l_y = trans(i)
        elif i in [3, 6, 9]:
            answer += 'R'
            r_x, r_y = trans(i)
        else:
            x, y = trans(i)
            l_dis = abs(l_x-x)+abs(l_y-y) 
            r_dis = abs(r_x-x)+abs(r_y-y)
    
            if l_dis < r_dis:
                answer += 'L'
                l_x, l_y = x, y
            elif l_dis > r_dis:
                answer += 'R'
                r_x, r_y = x, y
            elif l_dis == r_dis:
                if hand == 'right':
                    answer += 'R'
                    r_x, r_y = x, y
                else:
                    answer += 'L'
                    l_x, l_y = x, y
                    
            
                    
        
    return answer

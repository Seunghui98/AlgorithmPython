# 2019 카카오 겨울 인턴십 코딩테스트
# 이진탐색
def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    
    while left <= right:
        count = 0
        mid = (left+right) // 2
        for s in stones:
            if s - mid <= 0:
                count += 1
            else:
                count = 0
            
            if count == k:
                break
        
        if count < k:
            left = mid +1
            answer = max(answer, left)
        else:
            right = mid -1
    
        
    return answer

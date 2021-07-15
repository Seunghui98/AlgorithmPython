# 2019 카카오 겨울 인턴십 코딩테스트
# 순서
# 1. 모든 경우의 수를 구하기 위해 순열 사용
# 2. 순열 하나마다 banned_id와 매칭이 되는지 확인
#   2-1) 길이가 같은지 비교
#   2-2) 문자 하나씩 비교
#   2-3) '*'가 나올시 넘기고 같은문자인지 확인
# 3. 중복 제거 후 answer+=1


from itertools import permutations

def isMatch(user_set, banned_set):
    for i in range(len(user_set)):
        if len(user_set[i])!= len(banned_set[i]):     # 길이비교
            return False
        else:
            for j in range(len(user_set[i])):      # 문자 하나씩 비교
                if banned_set[i][j]=='*':    # '*'문자가 나올시 넘김
                    continue
                elif user_set[i][j] != banned_set[i][j]:     # 같은 문자인지 확인
                    return False
    return True

def solution(user_id, banned_id):
    ans=[]
    p_u=list(permutations(user_id, len(banned_id)))     # 순열

    for user_set in p_u:     # 한개의 순열: user_set
        if isMatch(user_set, banned_id):   # 적절한지 확인
            user_set=set(user_set)    # 중복제거   ex) frodo, crodo, abc123 와 crodo, frodo, abc123
            if user_set not in ans:   
                ans.append(user_set)

    return len(ans)

# 2019 카카오 겨울 인턴십 코딩테스트
#정확도O, 효율성O   O(N) 해쉬맵

#1. 현재 방 딕셔너리 생성
#2. 원하는 방이 비어있으면 딕셔너리에 추가 {원하는 방 : 원하는방+1}
#3. 원하는 방이 채워져있으면 재귀함수로 빈방 찾기 find_emptyroom(원하는 방+1)

#예시 room_number=[1,3,4,1,3,1]    
def find_emptyroom(chk, room_dict): # 재귀함수
    if chk not in room_dict.keys(): # 빈 방이면
        room_dict[chk] = chk+1 # rooms에 새 노드 추가
        return chk # 요청한 방
    empty = find_emptyroom(room_dict[chk], room_dict) # 재귀함수 호출
    room_dict[chk] = empty+1 # (배정된 방+1)을 부모노드로 변경
    return empty # 새로 찾은 빈 방

#테스트케이스
k=10
room_number=[1,3,4,1,3,1]

#현재 방 상태
room_dict={}
answer=[]
for i in room_number:
    room=find_emptyroom(i, room_dict)
    answer.append(room)
    print(room_dict)       
print(room_dict.keys())

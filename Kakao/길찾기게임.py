# 카카오 2019 코딩테스트 - 길찾기 게임
# 트리 -> 전위 순회, 후위 순회
import sys                                                                                                
sys.setrecursionlimit(10**6) #재귀함수 호출 횟수제한 막기 위해                                                          
                                                                                                          
preorder = list()                                                                                         
postorder = list()                                                                                        
                                                                                                          
def solution(nodeinfo):                                                                                   
    # 레벨 파악                                                                                               
    levels = sorted(list({x[1] for x in nodeinfo}), reverse=True)                                         
                                                                                                          
    # 노드좌표와 인덱스를 서로 연결                                                                                    
    # -x[1][1] : y좌표의 내림차순, x[1][0] : x좌표의 오름차순                                                           
    nodes = sorted(list(zip(range(1, len(nodeinfo)+1), nodeinfo)), key=lambda x:(-x[1][1], x[1][0]))      
                                                                                                          
    order(nodes, levels, 0)                                                                               
                                                                                                          
    return [preorder, postorder]                                                                          
                                                                                                          
                                                                                                          
# 전위 순회 : 부모 -> 왼 -> 오, 후위 순회 : 왼 -> 오 -> 부모                                                              
def order(nodeList, levels, curLevel):                                                                    
    n = nodeList[:]                                                                                       
    cur = n.pop(0) # 루트노드 꺼내기                                                                             
    preorder.append(cur[0]) # 그걸 preorder에 노드 번호 넣기                                                       
    if n:                                                                                                 
        for i in range(len(n)): # 남아 있는 리스트 중에서                                                           
                                                                                                          
            if n[i][1][1] == levels[curLevel+1]:                                                          
                if n[i][1][0] < cur[1][0]:                                                                
                    # x값이 작은 노드를 모두 가지고 다시 재귀 함수 선언                                                       
                    order([x for x in nodeList if x[1][0] < cur[1][0]], levels, curLevel+1)               
                else: # x값이 더 크면 오른쪽                                                                      
                    # x값이 더 큰 노드를 가지고 재귀함수 선언                                                             
                    order([x for x in nodeList if x[1][0] > cur[1][0]], levels, curLevel+1)               
                    break                                                                                 
                                                                                                          
    postorder.append(cur[0]) # 마지막에 postorder에 cur를 붙여주면 후위 순위가 완성                                        
                                                                                                          
                                                                                                          
                                                                                                          
                                                                                                          
print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))                                

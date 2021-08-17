# BOJ 겹치는 건 싫어 - 20922번
# 투포인터 정석 풀이
import sys                                                
                                                          
input = sys.stdin.readline                                
n, k = map(int, input().split())                          
data_list = [0] * 100001                                  
data = list(map(int, input().split()))                    
left = 0                                                  
max_value = 0                                             
                                                          
for i in range(len(data)):                                
    num = data[i]                                         
    data_list[num] += 1                                   
                                                          
    if data_list[num] > k:                                
        max_value = max(max_value, i - left)              
        while data_list[num] > k:                         
            data_list[data[left]] -= 1                    
            left += 1                                     
                                                          
    else:                                                 
        max_value = max(max_value, i - left+1)              
                                                          
                                                          
                                                          
print(max_value)                                          
                              

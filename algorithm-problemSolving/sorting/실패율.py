# 이코테 25번 실패율
def game(n, array):
  stage = []
  k = len(array)
  
  for i in range(1, n+1):
    count = array.count(i)
    if k == 0:
      percentage = 0
    else:
      percentage = count / k
      k -= count
    stage.append((percentage, i))
  stage.sort(key = lambda x:(-x[0], x[1]))
  
  for l in stage:
    print(l[1], end=' ')
  

n = int(input())
array = list(map(int, input().split()))
game(n, array)





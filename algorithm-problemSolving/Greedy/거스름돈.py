#예제 3-1 거스름돈 파이썬 풀이법
n = 1260
count = 0

#큰 단위의 화폐부터 차례대로 확인
coin_type = [500, 100, 50, 10]

for coin in coin_type:
	count += n // coin # 해당 화폐로 거슬러 줄 수 있을 동전의 개수 세기
    n %= coin 
    
print(count)

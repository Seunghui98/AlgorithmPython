# 기적의 매매법 - BOJ 20546
# 구현 - 단순하게 
import sys


input = sys.stdin.readline

money = int(input())

stock = list(map(int, input().split()))

bnp_money = money
timing_money = money
bnp_stock = 0
timing_stock = 0

for i in range(14):
    if(bnp_money // stock[i] > 0):
        bnp_stock += bnp_money // stock[i]
        bnp_money = (bnp_money % stock[i])


for i in range(14-3):
    if stock[i+3] < stock [i+2] < stock[i+1] < stock[i]:
        if (timing_money // stock[i+3] > 0):
            timing_stock += timing_money // stock[i+3]
            timing_money = (timing_money % stock[i+3])
    elif stock[i+3] > stock[i+2] > stock[i+1] > stock[i]:
        timing_money += (stock[i+3] * timing_stock)
        timing_stock = 0


bnp = bnp_stock * stock[13] + bnp_money
timing = timing_stock * stock[13] + timing_money
if bnp > timing:
    print("BNP")
elif bnp < timing:
    print("TIMING")
else:
    print("SAMESAME")




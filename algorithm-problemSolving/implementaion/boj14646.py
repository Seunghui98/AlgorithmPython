n = int(input())
menu = list(map(int, input().split()))

re = 0 
delete = 0
check = [False for _ in range((n*2)+1)]
sticker = []

for i in range(len(menu)):
    if check[menu[i]] is False:
        sticker.append(menu[i])
        check[menu[i]] = True
    else:
        delete += 1
    re = max(re, len(sticker) - delete)
    
print(re)

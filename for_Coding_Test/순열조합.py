# 조합
def combination(lst, n):
    result = []
    if n > len(lst):
        return result
    if n == 1:
        for i in lst:
            result.append([i])
    elif n > 1:
        for i in range(len(lst)-n+1):
            for temp in combination(lst[i+1:], n-1):
                result.append([lst[i]]+temp)
    return result

# 순열
def permutation(lst, n):
    result = []
    if n > len(lst):
        return result
    if n == 1:
        for i in lst:
            result.append([i])
    elif n > 1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in permutation(temp, n-1):
                result.append([lst[i]]+p)
    return result

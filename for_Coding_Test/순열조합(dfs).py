# 조합
def dfs_combination(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack = []
    for i in idx[:len(lst) - n + 1]:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()

        for i in range(cur[-1] + 1, len(lst) - n + 1 + len(cur)):
            temp = cur + [i]
            if len(temp) == n:
                element = []
                for i in temp:
                    element.append(lst[i])
                ret.append(element)
            else:
                stack.append(temp)
    return ret

# 중복 조합
def dfs_dul_combination(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack = []
    for i in idx[:len(lst) - n + 1]:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()

        for i in range(cur[-1], len(lst) - n + 1 + len(cur)):
            temp = cur + [i]
            if len(temp) == n:
                element = []
                for i in temp:
                    element.append(lst[i])
                ret.append(element)
            else:
                stack.append(temp)
    return ret

# 순열
def dfs_permutation(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack = []
    for i in idx:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()

        for i in idx:
            if i not in cur:
                temp = cur + [i]
                if len(temp) == n:
                    element = []
                    for i in temp:
                        element.append(lst[i])
                    ret.append(element)
                else:
                    stack.append(temp)
    return ret

# 중복 순열
def dfs_dul_permutation(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack = []
    for i in idx:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()

        for i in idx:
            temp = cur + [i]
            if len(temp) == n:
                element = []
                for i in temp:
                    element.append(lst[i])
                ret.append(element)
            else:
                stack.append(temp)
    return ret

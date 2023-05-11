# https://kpolyakov.spb.ru/school/ege/kege/train.htm?varId=2&select=7FFFFFF

def f(n, m):
    if n > m:
        return 0
    if n == m:
        return 1
    # if n % 2 != 0:
    #     return f(n * 4, m)
    return f(n + 2, m) + f(n * 3, m) + f(n * 4, m)


print(f(4, 600))
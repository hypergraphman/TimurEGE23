def alg(x):
    y1 = x % 2
    y2 = x % 3
    y3 = x % 5
    return y1 * 100 + y2 * 10 + y3


print(alg(55))
for i in range(10, 99 + 1):
    if alg(i) == 104:
        print(i)
        break

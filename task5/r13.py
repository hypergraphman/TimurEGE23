def alg(n):
    s1 = f'{n:b}'
    s2 = s1 + str(sum(map(int, s1)) % 2)
    s3 = s2 + str(sum(map(int, s2)) % 2)
    return int(s3, 2)


print(alg(28))
i = 1
while alg(i) <= 77:
    i += 1
print(i)
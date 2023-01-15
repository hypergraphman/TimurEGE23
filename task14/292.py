def n_to_p(n, p):
    r = ''
    while n > 0:
        d = '0123456789ABCDEF'[n % p]
        r = d + r
        n //= p
    return r


print(n_to_p(255, 16), hex(255))  # FF
print(n_to_p(194, 5))  # 1234
print(n_to_p(100, 2), bin(100))  # 1100100

for x in range(1, 100):
    n = 27**7 - 3**11 + 36 - x
    r = n_to_p(n, 3)
    s = sum(map(int, r))
    if s == 22:
        print(x)
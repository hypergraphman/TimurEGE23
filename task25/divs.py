def divs(n):
    s = {1, n}
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted(s)


print(sum(divs(100)))
def alg(n):
    d1, d2, d3 = n // 100, n // 10 % 10, n % 10
    nums = [d1 * 10 + d2, d2 * 10 + d1,
            d1 * 10 + d3, d3 * 10 + d1,
            d3 * 10 + d2, d2 * 10 + d3]
    filt_nums = []
    for num in nums:
        if 10 <= num <= 99:
            filt_nums.append(num)
    return max(filt_nums) - min(filt_nums)


print(alg(351))
i = 100
while alg(i) != 40:
    i += 1
print(i)

i = 999
while alg(i) != 40:
    i -= 1
print(i)

c = 0
for i in range(100, 999 + 1):
    if alg(i) == 40:
        print(i)
        c += 1
print(c)

for i in range(100, 1000):
    if alg(i) == 40:
        print(i)
        break

def alg(n):
    s1 = f'{n:b}'
    s2 = s1[1:]
    s3 = int(s2, 2)
    return n - s3


print(alg(11))
nums = set()
for i in range(500, 5000 + 1):
    nums.add(alg(i))
print(nums)
print(len(nums))

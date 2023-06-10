from fnmatch import fnmatch

for i in range(2023, 10**9, 2023):
    if fnmatch(str(i), '2*345?1'):
        print(i, i // 2023)
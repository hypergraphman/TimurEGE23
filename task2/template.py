print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                f = not(y <= x) or (z <= w) or not z
                if not f:
                    print(w, x, y, z)

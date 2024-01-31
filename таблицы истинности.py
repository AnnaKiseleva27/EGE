def f(x, y, z, w):
    return (not y or x) or not((not x or z) and (not z or x)) and not w

for x in range (0,2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if f(x, y, z, w) == 0:
                    print( x, y, z, w)

def golden_ratio(j):
    a, b = 1, 1
    for i in range(j - 1):
        a, b = b, b + a
    print(b / a)
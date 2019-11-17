def primenum(n):
    for a in range(1, n + 1):
        count = 0
        for i in range(2, a // 2 + 1):
            if (a % i == 0):
                 count += 1
        if (count <= 0):
            print(a)

primenum(1000)
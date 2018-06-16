m = [[0] * 8] * 8
md = ['Черный','Белый']
n = 0
for i in range(8):
    for r in range(8):
        if n == 0:
            while n < 1:
                m[i][r] = md[n]
                n += 1
        else:
            while n >= 1:
                m[i][r] = md[n]
                n -= 1
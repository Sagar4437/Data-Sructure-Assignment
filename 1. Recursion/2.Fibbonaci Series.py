def fibbonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    n_1_term = fibbonaci(n-1)
    n_2_term = fibbonaci(n-2)

    return n_1_term + n_2_term

for i in range(10):
    print(fibbonaci(i),end=' ')

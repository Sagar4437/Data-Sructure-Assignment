def Gsum(n):
    if n==0:
        return 1
    else:
        return 1/(2**n) + Gsum(n-1)

print(Gsum(0))



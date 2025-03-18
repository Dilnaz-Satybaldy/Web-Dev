N=int(input())
k = 0
while k <= N:
    if 2**k >= N:
        print(k)
        break
    k += 1

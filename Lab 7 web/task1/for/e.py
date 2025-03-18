x=int(input())
cnt = 0
while x > 0:
        cnt += x % 10
        x = x // 10
print(cnt)
n = int(input())  
array = map(int, input().split())  

cnt = sum(1 for num in array if num > 0)

print(cnt)

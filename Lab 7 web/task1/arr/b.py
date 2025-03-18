n = int(input())  
array = list(map(int, input().split()))  

even= list(filter(lambda x: x % 2 == 0, array))  
print(*even)  

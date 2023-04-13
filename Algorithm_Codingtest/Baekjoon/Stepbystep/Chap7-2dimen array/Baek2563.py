import sys
input = sys.stdin.readline


arr = [[0 for _ in range(100)] for __ in range(100)]

n = int(input())
for _ in range(n):
    x,y = map(int, input().split())
    for i in range(10):
        
        for j in range(10):
            arr[i+x][j+y] = 1
            
total = 0
for i in range(100):
    total += sum(arr[i])
print(total)

''''
이중배열의 sum은 리스트를 풀어줘야한다. 


print(sum(map(sum,a)))
이렇게도 할수있다
print(sum(sum(a[i])for i in r(100)))

'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
arr1 = [[0 for j in range(M)] for i in range(N)]

for k in range(N):
    a = list(map(int,input().split()))
    for l in range(M):
        arr1[k][l]= a[l]

for k in range(N):
    a = list(map(int,input().split()))
    for l in range(M):
        arr1[k][l] += a[l]
        
for _ in range(N):
    print(*arr1[_])


'''
2차원 배열 첫문제. 
for문 중첩으로 2차원 배열 만드는법을 배웠다. 
얕은복사 개념도 배웠다. [0]*n 으로 만들면 안됨

a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(n)]
와 엄청 깔끔하네
'''
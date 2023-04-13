import sys
input = sys.stdin.readline
maxvalue = -1
x = -1
y = -1
arr = []

for i in range(9):
    temp = list(map(int, input().split()))
    if max(temp) > maxvalue:
        maxvalue = max(temp)
        y = i
        x = temp.index(max(temp))

print(maxvalue)
print( y+1, x+1)


'''
2중 행렬을 깔끔하게 해버렸네
arr=[]
for i in range(9):
    arr+=list(map(int,sys.stdin.readline().split()))
    

'''
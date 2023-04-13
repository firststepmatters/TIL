import sys
input = sys.stdin.readline

n = int(input())
for i in range(1,n+1):    
    print(" "*(n-i) + "*"*(2*i-1))
for i in range(n-1,0,-1):
    print(" "*(n-i) + "*"*(2*i-1))

'''

실수를 너무 많이했음. 
오른쪽에도 스페이스를 달았음... 반성

'''
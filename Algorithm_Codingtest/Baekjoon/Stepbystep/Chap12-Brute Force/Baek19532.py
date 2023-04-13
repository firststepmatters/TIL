import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int,input().split())
s = a*e-b*d
print((c*e-f*b)//s,(a*f-c*d)//s)

'''
역행렬 

'''
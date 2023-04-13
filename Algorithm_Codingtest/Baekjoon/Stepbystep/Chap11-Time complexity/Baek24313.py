import sys
input = sys.stdin.readline

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())


if c-a1>0:
    if n0 >= a0/(c-a1) :print("1")
    else : print("0")
elif c-a1==0 :
    if a0 <= 0 : print("1")
    else : print("0")
else : print("0")

'''
r=1 if a*n+b<=c*n and c>=a else 0
조건을 되게 압축을 잘했다

생각해볼것

'''
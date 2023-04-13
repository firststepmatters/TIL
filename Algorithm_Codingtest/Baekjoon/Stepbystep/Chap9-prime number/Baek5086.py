import sys
input = sys.stdin.readline

while 1 == 1 :
    a,b = map(int,input().split())
    if a==0 and b==0 : break
    if a>b : 
        if a%b == 0 :
            print("multiple")
        else :
            print("neither")
    else:
        if b%a == 0 :
            print("factor")    
        else:
            print("neither")
            
'''
조건문을 너무 많이 쓴거같다.

while a!=0:
    if a%b==0:
        print('multiple')
    elif b%a==0:
        print('factor')
    else:
        print('neither')
이렇게 줄일수도 있다

'''
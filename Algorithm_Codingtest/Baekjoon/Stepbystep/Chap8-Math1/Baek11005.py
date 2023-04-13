import sys
input = sys.stdin.readline


numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int,input().split())

def binary(num):
    if num < B : print(numbers[num],end=""); return
    binary(num//B)
    leftover = num%B
    print(numbers[leftover],end="")

binary(N)

'''
진수변환은 결국 나누고 몫, 나머지의 반복이라
재귀함수를 사용했다. 

엄청 깔끔하게 풀었네
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = []
while n:
    result.append(tmp[n%b])
    n //= b

while result:
    print(result.pop(),end = '')

'''
import sys
input = sys.stdin.readline

print((2**int(input())+1)**2)
 
 
'''
쉬운문제니 해결방법은 노코멘트. 

연산 효율화에 있어서, 시간 절약한 사람은 
 
a = int(input())
s = 2
for i in range(a):
    s = s+s-1
print(s*s)

이렇게 풀었네. 나는 제곱 연산자가 2번 들어갔지만, 
이사람은 더하기를 위주로 해서 더 빠르게 돌렸네.

 
'''
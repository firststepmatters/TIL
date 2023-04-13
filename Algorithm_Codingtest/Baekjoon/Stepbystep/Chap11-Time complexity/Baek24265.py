import sys
input = sys.stdin.readline

a = int(input())
print(int(a*(a-1)/2),"\n2")

'''
간만에 펜들고 계산해봄

i -> 1 ~ (n-1) : n-1개
j -> (i+1)-> n : n-i개

이때 i를 중심으로 전개해보면, 

i:  1    2    3   ...  n-1
j: n-1  n-2  n-3  ...   1
이 된다. 우리가 알고싶은것은 연산 J의 횟수이므로.. 이를 더하면 된다. 
1~n-1의 합

'''
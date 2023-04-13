import sys
input = sys.stdin.readline

N = int(input())
total = []
for _ in range(N):
    a,b = map(int,input().split())
    total.append([b,a])

total.sort()
for __ in range(N):
    print(total[__][1],total[__][0])



'''
이건 11650 과 똑같은 풀이방법인데 순서만 바꾼것.
11650에서 배운 방식으로 풀어보자

'''
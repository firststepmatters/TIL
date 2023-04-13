import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bags = [0]*N

for i in range(M):
    a,b,c = map(int,input().split())
    for j in range(a-1,b):
        bags[j] = c
print(*bags)

# 문제는 다 풀어놓고 list 대괄호로 출력해서 틀렸음.
# *list 방법이 제일 편해보임 뒤에 sep="\n" 등으로 나눌수있음
# for x in range (N) :
#    print(arr[x],'',end='')
#같은 방식도 씀.
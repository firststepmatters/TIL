import sys
input = sys.stdin.readline

total = [1,1,2,2,2,8]
ans = list(map(int,input().split()))

a = [total[i] - ans[i] for i in range(6)]
print(*a)

'''
리스트끼리의 연산에는 두가지 방법이 있음. 
하나는 위에서 커버한 List comprehension

두번째는 Zip. 

[x+y for x,y in zip(list1,list2)]

근데 list comprehension이 더 외우기 쉬운거같음

'''
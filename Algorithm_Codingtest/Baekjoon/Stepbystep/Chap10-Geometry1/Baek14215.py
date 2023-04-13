import sys
input = sys.stdin.readline

cases =list(map(int,input().split()))
cases.sort()
aaa = cases[0]+cases[1]
if cases[2] >= aaa:
    print(aaa+aaa-1)
else:
    print(sum(cases))
    
'''
l = sorted(list(map(int,input().split())))
print(min(sum(l), 2*(l[0]+l[1])-1))
압축 잘했다.
리스트 정렬해서 받는건 기억해두면 쓰기 좋겠다


'''
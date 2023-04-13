import sys
input = sys.stdin.readline
N = int(input())
a = sorted(list(list((map(int,input().split()))) for _ in range(N)))
for i in range(N):
    print(*a[i])
    
    
'''
본격적인 정렬 시작.

lst = sys.stdin.readlines()[1:]
lst.sort(key=lambda x: int(x.split()[1]))
lst.sort(key=lambda x: int(x.split()[0]))
print(''.join(lst))

이런건 이해도 안된다. 

이해할수있는 풀이는,

def cond(dot):
    x, y = dot.split()
    return int(x) + int(y)/1000000

dots = sorted(sys.stdin.readlines()[1:], key=lambda x: cond(x))
print(''.join(dots))

인풋 변수 크기가 정해져있으니, 소수로 밀어넣고 정렬하기. 
좋은 생각이다.




'''
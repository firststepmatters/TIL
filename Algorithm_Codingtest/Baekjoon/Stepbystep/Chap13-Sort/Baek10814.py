import sys
input = sys.stdin.readline

N = int(input())
arr = [input().split() for _ in range(N)]
arr.sort(key= lambda x: int(x[0]))

for i in range(N):
    print(*arr[i])
    
'''

틀린이유 한참고민했음. 
이유는 나이가 str 변수로 들어가서, 정렬시 

120살이 21살보다 빠르게 나옴 -> 사전순. 
람다에 int변수 걸어줘서 해결

'''
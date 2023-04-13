import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [i for i in range(1,N+1)] 
#많이 쓸것같으니 외워두자
for _ in range(M):
    a,b = map(int, input().split())
    temp = []
    for i in range(a-1,b):
        temp.append(arr[i])
    for j in range(a-1,b):
        arr[j] =temp.pop()    
print(*arr)
        
'''
이번 풀이는. 리스트를 역으로 하는것을 하기위해 
스택 FILO를 사용해서 임시 리스트 temp에 
순서대로 넣고 마지막순으로 뺀걸 arr에 넣었음.
 
    s[i-1:j] = s[i-1:j][::-1]
    이런 풀이도 있음.
나는 저게 중간에 겹쳐질것 같았는데 상관이 없나?
 

'''
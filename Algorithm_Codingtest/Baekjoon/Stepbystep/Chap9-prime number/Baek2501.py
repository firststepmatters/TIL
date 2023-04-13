import sys
input = sys.stdin.readline

N, K = map(int,input().split())
iterations = 0
nums = 0
while iterations < N :
    iterations += 1
    if N%iterations == 0 : nums +=1
    if nums == K : 
        print(iterations)
        break
    if iterations == N :
        print("0")
    
'''

try:
    print(sorted([i for i in range(1,n+1)if n%i==0])[k-1])
except:
    print(0)
    
다양한 풀이가 있네

a,b=map(int,input().split())
print(([f'{i}'for i in range(1,a+1)if a%i<1]+[0]*10000)[b-1])

'''
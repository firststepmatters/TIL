import sys
input = sys.stdin.readline

def sol(N):
    n = 0
    ans = []
    while n< N//2+1:
        n += 1
        if N%n ==0 : ans.append(n)
    if sum(ans) == N :
        print(N, "= ",end="")
        print(*ans, sep=" + ")
    else :
        print(N,"is NOT perfect.")


a = int(input())
while a != -1:
    sol(a)
    a = int(input())

'''
내풀이는 약 60ms 36ms는 어떻게 한거지

약수 구하기
def yaksu(n):
    ys = {1}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ys.add(i)
            ys.add(n // i)
    return ys
약수 조건범위가 난 너무 넓네. 
제곱근까지 찾은다음 그거 양옆으로 더해버리는구나
난 순서대로 구하니깐 sort는 안하지만, 대신 sort하고


'''
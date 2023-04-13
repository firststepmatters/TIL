import sys
input = sys.stdin.readline
N= int(input())
times = 1
num = 666
while times != N:
    num += 1
    if "666" in str(num) :
        times += 1
print(num)

'''
예전에 규칙 찾으려다 포기한 문제. 
브루트포스를 사용하면 간단하게 풀린다.
고집 부리지말고 브루트포스를 써야할땐 쓰자. 
결국 컴퓨터는 브루트포스가 기반이니깐. 
시행횟수를 줄일수 있는 방법을 고민해야함
'''
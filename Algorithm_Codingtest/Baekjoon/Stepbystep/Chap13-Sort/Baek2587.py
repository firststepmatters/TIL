import sys
input = sys.stdin.readline

a = sorted([int(input()) for _ in range(5)])
print(sum(a)//5, a[2],sep="\n")
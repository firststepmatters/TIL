import sys
input = sys.stdin.readline

N= int(input())
N_card = set(map(int,input().split()))

M = int(input())
M_card = list(map(int,input().split()))

for i in range(M):
    if M_card[i] in N_card : print("1", end=" ")
    else : print("0", end=" ")
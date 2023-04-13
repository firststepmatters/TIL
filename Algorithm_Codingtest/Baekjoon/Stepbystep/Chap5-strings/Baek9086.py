import sys
input = sys.stdin.readline

for _ in range(int(input())):
    word = input().strip()
    print(word[0],word[-1], sep="")

'''
	print(X[0]+X[-1])
 이렇게도 가능하네..
 
'''
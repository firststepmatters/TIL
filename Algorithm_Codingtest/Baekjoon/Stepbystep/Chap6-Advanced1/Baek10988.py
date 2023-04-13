import sys
input = sys.stdin.readline
test = 0
word = input().strip()
for i in range(len(word)//2):
    if word[i] != word[-(i+1)]:
        test +=1
        
if test == 0:
    print("1",end="")
else:
    print("0",end="")
    
'''

틀린이유 한참 고민했음. 
원인은 input()에서 strip 하지않아 끝부분에 공백
strip 빼먹지 말기, 공백 관리 잘하기.

word = list(input())
word_reverse = list(reversed(word))
다른사람들은 그냥 문자열 역전 파이썬 함수 사용

'''
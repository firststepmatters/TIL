import sys
input = sys.stdin.readline

N, B = list(input().split())
sum = 0
for i in range(len(N)):   
    if ord(N[i]) > 64:
        sum +=  (ord(N[i])-55)*(int(B)**(len(N)-i-1))
    else:
        sum +=  int(N[i])*(int(B)**(len(N)-i-1))
print(sum)



'''
처음에 문자와 숫자가 섞인 str에서 
숫자만 건지기 힘들어서 유니코드를 사용함. 
유니코드 값이 일정이상이면 글자, 아니면 int변환
나머지는 평이한거같음. 

유니코드 안쓸거면, 0~9,A~Z의 문자열 만들고
인덱스 서치해서 숫자 찾기


파이썬 int n진법 10진법 변환 가능
int(변환할string, n진법)
이런 풀이가 있네
'''
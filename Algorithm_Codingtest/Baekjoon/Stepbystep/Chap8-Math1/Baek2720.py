import sys
input = sys.stdin.readline


for _ in range(int(input())):
    money = int(input())
    print(money//25,end=" ")
    money = money%25
    print(money//10,end=" ")
    money = money%10
    print(money//5,end=" ")
    money = money%5
    print(money)
    
    '''
    
           quarter, n = divmod(n, 25)
        dime, n = divmod(n, 10)
        nickel, n = divmod(n, 5)
        penny = n
    
    이게 제일 예쁜 풀이인것같다.
    
    '''
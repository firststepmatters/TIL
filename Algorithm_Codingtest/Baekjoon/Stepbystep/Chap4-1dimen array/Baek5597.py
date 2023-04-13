import sys
input = sys.stdin.readline

total = set(range(1,31))
students = set()
for _ in range(28):
    students.add(int(input()))

print(*sorted(list(total - students)))

'''
이번 문제는 set을 써보라고 한느낌. 
print(*{*map(int,open(0))}^{*range(1,31)}) 이런건 이해도 안됨

for i in range(28):
    x.remove(int(input()))
    지우는 풀이도 가능하긴함 
    
'''

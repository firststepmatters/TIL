import sys
input = sys.stdin.readline


N = int(input())

a = (list(set(input().strip() for _ in range(N))))
total = sorted(a)
total.sort(key=len)

print(*total,sep="\n")

'''

total2 = map(lambda x: list(x).append(len(x)), total)
lambda x : print(x), range(5)
print(list(total2))
print(total2)
'''
#total = sorted(list(input().strip() for _ in range(N)),key = str.lower)
#print(*total,sep="\n")



'''
람다 함수식을 만들면서 실수한점. 
계속 람다식내부에서 none 이 리턴 => 이유는 list.append를 했는데, append 는 리턴이 none 이기 때문. 

이중 정렬을 하는법을 배웠다. 
람다 쓰는법도 좀 배웠다. 
key를 잘 써먹어야겠다. 



'''
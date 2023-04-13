N, M = list(map(int,input().split()))
arr = [x for x in range(1,N+1)]

for _ in range(M):
    b,e,m = list(map(int,input().split()))
    order = arr[m-1:e] + arr[b-1:m-1]
    temp = []
    for plz in order:
        arr[int(plz)]
    for j in range(b-1,e):
        arr[j] = temp.pop


'''
개 애 미 시 발

For문 안에서, range 자리에 리스트를 가져온다
이후 인덱스(리스트 내부값)을 사용해 
다른 리스트 arr 의 값을 가져오려 하면 에러.

'''
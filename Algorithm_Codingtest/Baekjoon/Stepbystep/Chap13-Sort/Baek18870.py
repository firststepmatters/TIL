import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
s_arr = sorted(set(arr))
arr_dic ={}
n=0
for i in s_arr:
    arr_dic[i]=n
    n+=1

arr_dic2 = {s_arr[i]:i for i in range(len(s_arr))}

print(arr_dic)
print(arr_dic2)


'''
시간초과가 떳다. 

시간초과의 원인-> list.index() = O(N)
print(*list(map(lambda x : s_arr.index(x), arr)))

풀이방법은 Dict 사용 -> O(1)



'''
#역수열
import sys
sys.stdin=open("input10.txt","r")
n= int(input())
a=list(map(int, input().split()))
a.insert(0,0) #밑에꺼 사용하는거
seq=[0]*n
# for i in range(n):
#     for j in range(n):
#         if a[i]==0 and seq[j]==0:
#             seq[j]=i+1
#             break
#         elif seq[j]==0:
#             a[i] -=1

# for x in seq:
#     print(x, end=' ')

for i in range(1, n+1):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i
            break
        elif seq[j] == 0:
            a[i] -= 1

for x in seq:
    print(x, end=' ')

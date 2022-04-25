#창고 정리
import sys
sys.stdin=open("input7.txt","r")
L=int(input())
a=list(map(int, input().split()))
m=int(input())
a.sort()
for _ in range(m):
    a[0]+=1
    a[L-1] -=1
    a.sort()

print(a[L-1]-a[0])
#수들의 조합
import sys
import itertools as it
sys.stdin=open("input15.txt","r")
n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0
for x in it.combinations(a,k): #조합 a라는 리스트에서 k개를 뽑아서 보여줌
    #print(x)
    if sum(x)%m==0:
        cnt+=1
print(cnt)

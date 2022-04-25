#바둑이 승차(DFS)

import sys
from collections import deque

sys.stdin = open("input07.txt","r")

def DFS(L, sum, tsum): #L:a 리스트를 접근하는 index 번호 ,sum: 부분집합 합
    global result
    if sum +(total-tsum) < result:
        return #total - tsum : 앞으로 판단해야할 바둑이들의 무게
    if sum>c: #시간 제한을 위해 제한을 더 걸어야함
        return

    if L==n:
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum+a[L], tsum+a[L])
        DFS(L+1, sum, tsum+a[L])


if __name__ =="__main__":
    c, n = map(int, input().split())
    a=[0]*n
    result=-2147000000
    for i in range(n):
        a[i]=int(input())
    total = sum(a)
    DFS(0,0,0)
    print(result)
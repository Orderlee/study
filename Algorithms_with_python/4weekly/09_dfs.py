#동전 교환

import sys
sys.stdin = open("input09.txt","r")

def DFS(L,sum):
    global res
    if L>res: #레벨보다 res보다 크면 탐색 할 필요가 없음
        return
    if sum>m:
        return
    if sum == m:
        if L<res:  # res가 지역변수
            res=L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])





if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res=2147000000
    a.sort(reverse=True)
    DFS(0,0)
    print(res)

#부분집합 구하기
#상태트리
import sys

sys.stdin = open("input04.txt","r")

def DFS(x):
    if x == n+1:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')

    else:
        ch[x]=1
        DFS(x+1)
        ch[x]=0
        DFS(x+1)


if __name__=="__main__":
    n = int(input())
    ch=[0]*(n+1)
    DFS(1)
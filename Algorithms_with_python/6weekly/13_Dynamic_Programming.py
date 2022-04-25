#회장뽑기(플로이드-워샬 응용)

import sys
sys.stdin = open("input13.txt","r")

if __name__ =="__main__":
    n = int(input())
    dis =[[100]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dis[i][i] =0
    while True:
        a , b = map(int, input().split())
        if a==-1 and b==-1:
            break
        dis[a][b]=1
        dis[b][a]=1


    for k in range(1, n+1): #플로이드 워샬 알고리즘
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])
    # for x in dis:
    #     print(x)
    res =[0]*(n+1)
    score=100
    for i in range(1,n+1):
        for j in range(1, n+1):
            res[i]=max(res[i], dis[i][j])
        score = min(score,res[i]) #최소값이 회장후보

    out=[] #회장후보
    for i in range(1, n+1):
        if res[i] == score:
            out.append(i)

    print("%d %d" %(score, len(out)))
    for x in out:
        print(x, end=' ')
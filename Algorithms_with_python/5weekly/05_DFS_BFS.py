#동전 분배하기(DFS)

#DFS 문제 풀때는 상태트리 그려가면서 생각하기

import sys
sys.stdin = open("input05.txt","r")

def DFS(L):
    global res
    
    if L == n:
        cha = max(money)-min(money)
        if cha<res:
            tmp = set()
            for x in money:
                tmp.add(x) #중복을 허용하지 않음
            if len(tmp) ==3:
                res=cha


    else: #가지 뻗어나가는 곳
        for i in range(3):
            money[i]+= coin[L]
            DFS(L+1)
            money[i]-=coin[L]







if __name__=="__main__":
    n = int(input()) #동전의 개수
    coin=[]
    money=[0]*3 # 각 사람 금액
    res = 2147000000
    for _ in range(n):
        coin.append(int(input()))

    DFS(0)
    print(res)

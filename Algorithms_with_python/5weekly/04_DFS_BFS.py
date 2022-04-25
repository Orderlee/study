#동전 바꿔주기(DFS)

import sys
sys.stdin = open("input04.txt","r")

def DFS(L, sum):
    global cnt
    if sum> T:
        return
    if L==k:
        if sum ==T:
            cnt +=1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum+(cv[L]*i))




if __name__ == "__main__":
    T = int(input()) # 지폐금액
    k = int(input()) # 동전가지수
    cv = list() #동전 금액
    cn = list() #동전 개수
    for i in range(k):
        a, b = map(int, input().split()) #a 금액, b개수
        cv.append(a)
        cn.append(b)

    cnt = 0
    DFS(0,0)
    print(cnt)
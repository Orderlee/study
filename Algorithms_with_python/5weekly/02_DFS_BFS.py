#휴가 (DFS 활용)

import sys
sys.stdin = open("input02.txt","r")

def DFS(L,sum): #L은 T와 P에 접근하는 인덱스겸 날짜
    global res
    if L == n+1:
        if sum > res:
            res = sum

    else:
        if L+T[L]<= n+1: #상담하는 날
            DFS(L+T[L], sum+P[L])
        DFS(L+1, sum)


if __name__ =="__main__":
    n = int(input()) #날짜
    T = list() #시간
    P = list() #얻을 수 있는 금액

    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)

    res = -2147000000
    T.insert(0,0) #인덱스번호를 날짜로 사용하기 때문에 0,0 을 insert 함
    P.insert(0,0)
    DFS(1,0) #날짜, 금액
    print(res)
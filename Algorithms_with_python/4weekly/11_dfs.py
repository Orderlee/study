# 수열 추측하기
# 답이 여러개 나올 시 가장 앞에오는 것을 출력

import sys
sys.stdin = open("input11.txt","r")
def DFS(L,sum): #L:, sum: 최종 총합
    if L==n and sum==f:
        for x in p:
            print(x, end=' ')
        #print() #가장 앞에나오는 값 확인
        sys.exit(0) #출력후 프로그램 종료
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                p[L]=i
                DFS(L+1, sum+(p[L]*b[L])) #p에 i가 들어가도 됨
                ch[i]=0


if __name__ =="__main__":
    n, f = map(int, input().split())
    p=[0]*n
    b=[1]*n
    ch=[0]*(n+1)
    for i in range(1,n): #b[i] = (b[i-1]*(n-i))//i
        b[i] = b[i-1]*(n-i)//i
    DFS(0,0)
    # for x in b: # b확인, 이항계수 초기화 확인
    #     print(x, end=' ')

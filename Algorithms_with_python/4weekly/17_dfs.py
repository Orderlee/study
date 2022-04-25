#경로 탐색(그래프DFS)

import sys
sys.stdin = open("input17.txt","r")
def DFS(v): # v는 노드번호
    global cnt
    if v==n:
        cnt +=1
        #for x in path: #경로 확인용
            #print(x, end=' ')
        #print()
    else: #상태트리 가지가 뻗어야함
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i]==0:
                ch[i]=1
                #path.append(i) #경로확인
                DFS(i)
                #path.pop() #뒤로 이동했을시 빼야함
                ch[i]=0




if __name__ == "__main__":
    n,m = map(int, input().split())
    g=[[0]*(n+1) for _ in range(n+1)]
    ch=[0]*(n+1)
    for i in range(m):
        a , b = map(int, input().split())
        g[a][b] = 1

    cnt = 0
    #path=[]
    #path.append(1)
    ch[1]=1
    DFS(1)
    print(cnt)
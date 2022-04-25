# 피자 배달 거리 (DFS활용)
import sys
sys.stdin=open("inpuy17.txt","r")
def DFS(L,s):
    global res
    if L==m:

        # for x in cb:
        #     print(x, end=' ')
        # print()
        sum =0 #도시의 피자거리
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1-x2)+abs(y1-y2))
            sum +=dis

        if sum<res:
            res = sum
    else:
        for i in range(s, len(pz)):
            cb[L]=i
            DFS(L+1, i+1)


if __name__ =="__main__":
    n, m = map(int, input().split()) #n: 도시지도정보 격자크기, m:살아남을 피자집 갯수
    board = [list(map(int, input().split())) for _ in range(n)] #도시 지도 정보
    hs = [] #집 좌표정보
    pz = [] #피자집 좌표정보
    cb=[0]*m
    res = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                hs.append((i,j))
            elif board[i][j] ==2:
                pz.append((i,j))
    DFS(0,0)
    print(res)
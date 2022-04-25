#안전영역(BFS)
# 격자판 탐색하면서 특정 영역 넓이 찾는것들은 DFS나 BFS 둘다 가능


import sys
sys.stdin = open("input14.txt","r")
dx = [-1,0,1,0]
dy = [0,1,0,-1]
sys.setrecursionlimit(10**6)

def DFS(x,y,h):
    ch[x][y] = 1
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>h: # 지도정보
            DFS(xx,yy,h)


if __name__ =="__main__":
    n = int(input())
    cnt = 0 #안전영역이 몇개인가
    res = 0 #최종적인 답
    board = [list(map(int,input().split())) for _ in range(n)]
    for h in range(100):
        ch=[[0]*n for _ in range(n)]
        cnt=0 #안정영역이 바뀌면 카운트 다시 해야함
        for i in range(n):
            for j in range(n):
                if ch[i][j] ==0 and board[i][j]>h: # h 보다 커야지 물에 안잠긴 육지, 안전영역
                    cnt +=1
                    DFS(i,j,h) # 현재지점에서 h가 클때만 퍼져나가기 위한 조건을 같이 넘김
        res = max(res, cnt)
        if cnt ==0:
            break
    print(res)

#미로탐색(DFS)
# 한곳으로 뻗어나가 도착지점 도착 후 다시 돌아가서 다른길 찾음
# 돌아갈떈 체크를 풀어서 다시 돌아가게끔 해야함

import sys
sys.stdin = open("input10.txt","r")
dx=[-1,0,1,0]
dy= [0,1,0,-1]
def DFS(x,y):
    global cnt
    if x==6 and y ==6: #도착지점
        cnt+=1
    else:
        for i in range(4):
            xx = x+dx[i] #앞으로 갈 방향
            yy = y+dy[i] #앞으로 갈 방향
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0: #방향 탐색, board 방문하지 않은 곳이어야함
                board[xx][yy]=1
                DFS(xx,yy)
                board[xx][yy]=0 # 되돌아가면서 board 값을 취소 해야함, 벽을 허뭄




if __name__ == "__main__":
    board=[list(map(int,input().split())) for _ in range(7)] #격자판 정보
    cnt = 0
    board[0][0] =1 #첫 출발점
    DFS(0,0)
    print(cnt)
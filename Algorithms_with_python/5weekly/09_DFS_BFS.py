#미로의 쵣단거리 통로(BFS 활용)

import sys
from collections import deque

sys.stdin = open("input09.txt","r")
dx=[-1,0,1,0]
dy = [0,1,0,1]
board = [list(map(int,input().split())) for _ in range(7)]
dis = [[0]*7 for _ in range(7)]
Q=deque()
Q.append((0,0)) #좌표 출발점
board[0][0] =1 #한번 방문하면 벽으로 만듬 이동하지 못하게
while Q:
    tmp=Q.popleft()
    for i in range(4):
        x = tmp[0]+dx[i] #방향을 보는것
        y = tmp[1]+dy[i] #방향을 보는것
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:  #경계선 밖으로 나가지 않게 영역 지정, 및 벽으로 만듬
            board[x][y] =1 #체크 효과가 남
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x,y)) #Q가 계속 돔

if dis[6][6] ==0: #
    print(-1)
else:
    print(dis[6][6])

# 섬나라 아일랜드(BFS 활용)
# 단지번호 붙이기와 비슷

import sys
from collections import deque
sys.stdin = open("input13.txt","r")
dx = [-1,-1,0,1,1,1,0,-1] # 8방향 탐색 시계방향으로 탐색하게끔
dy = [0,1,1,1,0,-1,-1,-1]

n = int(input()) #격자 갯수
board=[list(map(int, input().split())) for _ in range(n)] #nxn 지도 정보를 받음
cnt = 0
Q=deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] =0
            Q.append((i,j))
            while Q:
                tmp =Q.popleft()
                for k in range(8): #8방향으로 돌아서 8
                    x = tmp[0]+dx[k]
                    y = tmp[1]+dy[k]  #x,y 갈려는 방향 좌표 계산
                    if 0<=x<n and 0<=y<n and board[x][y] ==1: # board값이 1이어야 퍼져 나감, 0은 퍼져나가면 안됌
                        board[x][y]=0
                        Q.append((x,y))
            cnt +=1 # 섬의 갯수

print(cnt)



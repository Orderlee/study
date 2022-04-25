#등산경로(DFS)
#앞전에 배웠던 미로탐색과 거의 유사
#차이점은 출발점과 도착점이 입력에 따라 달라짐
#현재 지점 보다 앞으로 가야할 값이 커야 갈 수 있음
#되돌아갈 때 체크를 풀어야함

import sys
sys.stdin = open("input11.txt","r")
dx = [-1,0,1,0]
dy = [0, 1, 0 ,-1]

def DFS(x,y):
    global cnt
    if x == ex and y == ey: #도착지점
        cnt +=1
    else:
        for k in range(4):
            xx = x+dx[k]
            yy = y+dy[k]
            if 0 <=xx<n and 0<=yy<n and ch[xx][yy]== 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy]=1
                DFS(xx,yy)
                ch[xx][yy]=0 #되돌아 갔을 때,

if __name__ =="__main__":
    n = int(input()) # 격자판의 크기
    board = [[0]*n for _ in range(n)] #등고선 정보
    ch = [[0]*n for _ in range(n)] #체크리스트 (경로)
    max = -2147000000 #등고선의 최대 최소를 찾아야하기 떄문에 초기화
    min = 2147000000
    for i in range(n): #실제 입력 되는 곳
        tmp = list(map(int, input().split()))
        for j in range(n): #tmp 접근
            if tmp[j]<min: #최소값 발견
                min = tmp[j]
                sx = i #출발지점
                sy = j #출발지점
            if tmp[j]>max:
                max = tmp[j]
                ex = i #도착지점
                ey = j #도착지점
            board[i][j] = tmp[j]
    ch[sx][sy]=1
    cnt=0
    DFS(sx,sy)
    print(cnt)

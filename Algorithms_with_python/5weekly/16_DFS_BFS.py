#사다리 타기(DFS)
# 도착지점 열을 탐색 후 역으로 추적

import sys
sys.stdin = open("input16.txt","r")
def DFS(x,y):
    ch[x][y] = 1
    if x==0:
        print(y) #열번호
    else:
        if y-1>=0 and board[x][y-1]==1 and ch[x][y-1]==0: #방문 안한곳이 있어야함
            DFS(x, y-1)
        elif y+1<10 and board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        else:
            DFS(x-1, y)



if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0]*10 for _ in range(10)]
    for y in range(10):
        if board[9][y]==2:
            DFS(9,y)

#사과나무(BFS)

import sys
from collections import deque
sys.stdin = open("input08.txt","r")
dx = [-1,0,1,0]
dy=[0,1,0,-1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
sum = 0
Q=deque()
ch[n//2][n//2]=1
sum+=a[n//2][n//2]
Q.append((n//2,n//2))
L=0
while True:
    if L==n//2:
        break
    size = len(Q)
    for i in range(size): # size :레벨
        tmp = Q.popleft()
        for j in range(4): #퍼져 나가는 곳
            x = tmp[0]+dx[j] #
            y = tmp[1]+dy[j]
            if ch[x][y]==0: #체크배열, 탐색한지점이 이미 방문하면 안됨 0이 되었을 때 sum에다가 누적
                sum+=a[x][y]
                ch[x][y]=1 #방문했다고 체크
                Q.append((x,y)) #튜플로 입력


    # print(L, size) # 출력하여 확인 #레벨2되면 브레이크
    # for x in ch:
    #     print(x)
    L+=1
print(sum)
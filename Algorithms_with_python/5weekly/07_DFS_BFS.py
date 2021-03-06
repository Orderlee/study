#송아지 찾기 (BFS: 상태트리탐색)
#BFS: 넓이 우선 탐색 (레벨 탐색을함)

import sys
from collections import deque
sys.stdin = open("input07.txt","r")
MAX = 10000 #좌표
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
n,m = map(int,input().split())
ch[n] = 1
dis[n] =0
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    if now ==m:
        break
    for next in (now-1, now+1, now+5):
        if 0<next<=MAX:
            if ch[next] ==0:
                dQ.append(next)
                ch[next] =1
                dis[next] = dis[now]+1
print(dis[m])
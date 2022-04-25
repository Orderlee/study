#공주구하기(큐 자료구조로 해결)

import sys
from collections import deque #deque 자료구조
sys.stdin = open("input24.txt","r")
n , k = map(int, input().split())
dq=list(range(1, n+1))
#print(dq)
dq = deque(dq)
while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()



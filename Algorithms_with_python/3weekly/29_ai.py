#최소힙
import sys
import heapq as hq
sys.stdin = open("input29.txt","r")
a=[]

while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a) ==0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n) # a라는 리스트에 n값을 밀어라


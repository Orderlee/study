#최대 선 연결하기 #최대부분증가수열과 일치함
#최소 몇개의 선을 제거고 교차하지 않는 선 갯수를 구해보아라: 전체 갯수에서 최대부분증가수열을 빼면 됨
import sys
sys.stdin = open("input05.txt","r")

n = int(input())
arr =list(map(int, input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1
res = 0

for i in range(2,n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if arr[j]<arr[i] and dy[j] > max:
            max = dy[j]

    dy[i] = max+1
    if dy[i]>res:
        res = dy[i]

print(res)

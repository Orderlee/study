#동적계획법 네트워크 선 자르기 #bottom-up방식
#f(n) = f(n-2)+f(n-1) 방식으로 공식 화 하면 됨
import sys
sys.stdin = open("input.txt","r")
n = int(input())
dy=[0]*(n+1)
dy[1]=1
dy[2]=2
for i in range(3,n+1):
    dy[i] = dy[i-1]+dy[i-2]

print(dy[n])
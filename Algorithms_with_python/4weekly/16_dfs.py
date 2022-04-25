#인접행렬(가중치 방향 그래프)
#노드와 간선(노드와 노드연결)의 집합 = 그래프
#간선에 방향이 있다면 방향 그래프
#간섭값까지 있다면 가중치 방향그래프라 한다
#인접행렬은 행번호에서 열번호로 이동
import sys
sys.stdin = open("input16.txt","r")
n,m = map(int, input().split())
g=[[0]*(n+1) for _ in range(n+1)] #그래프
for i in range(m):
    a, b,c = map(int,input().split()) #c는 가중치
    #g[a][b]=1 #무방향 그래프
    #g[b][a]=1 #무방향 그래프
    g[a][b]=c #가중치 방향 그래프
for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()







# 무방향 input16에 넣을 데이터
# 5 5
# 1 2
# 1 3
# 2 4
# 3 4
# 4 5

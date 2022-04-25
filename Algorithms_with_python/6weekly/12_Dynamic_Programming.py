#플로이드 워샬 알고리즘
#dis[i][j] : i노드에서 j노드 가는데 최소 비용값

#min 1) dis[i][j]
#min 2) dis[i][k]+dis[k][j]  #1번값과 2번값 중 최소값을 사용


import sys
sys.stdin = open("input12.txt","r")

if __name__ == "__main__":
    n, m = map(int, input().split()) #n:정점 번호 m: 간선의 갯수
    dis= [[5000]*(n+1) for _ in range(n+1)] #2차원 다이나믹 테이블 dis
    for i in range(1, n+1):
        dis[i][i] =0
    for i in range(m): #인접 행렬을 만드는 For문, 중간 거치는 곳이 없음
        a, b, c = map(int, input().split())
        dis[a][b] = c
    for k in range(1, n+1): #플로이드 워샬 알고리즘(3중 for 문)
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dis[i][j] == 5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')
        print()

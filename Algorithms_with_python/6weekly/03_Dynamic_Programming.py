#계단 오르기(Top-Down: 메모이제이션)

import sys
# sys.stdin = open("input03.txt","r")
# def DFS(len):
#     # 가지자르기
#     if dy[len] > 0:
#         return dy[len]
#     #
#     if len == 1 or len == 2:
#         return len
#     else:
#         dy[len] = DFS(len - 1) + DFS(len - 2)
#         return dy[len]
#
#
# if __name__ == "__main__":
#     n = int(input())
#     dy = [0] * (n + 1)
#     print(DFS(n))

#돌다리 건너기 (bottom-up)
sys.stdin = open("input03.txt","r")

n = int(input())
dy=[0]*(n+2)
dy[1]=1
dy[2]=2
for i in range(3,n+2):
    dy[i] = dy[i-1]+dy[i-2]

print(dy[n+1])
#가장 높은 탑 쌓기

import sys
sys.stdin = open("input06.txt","r")
if __name__ == "__main__":
    n = int (input())
    bricks=[]
    for i in range(n):
        a, b, c = map(int, input().split()) #a:밑면 넓이, b:벽돌의 높이, c:무게
        bricks.append((a,b,c))
    bricks.sort(reverse=True)
    dy=[0]*n
    dy[0] = bricks[0][1] #[벽돌번호][0:밑면넓이, 1:벽돌의 높이, 2:무게]
    res = bricks[0][1];
    for i in range(1,n): # i는 가장 상단 벽돌
        max_h = 0;
        for j in range(i-1, -1, -1):
            if bricks[j][2]>bricks[i][2] and dy[j]>max_h:
                max_h = dy[j]
        dy[i] = max_h+bricks[i][1]
        res = max(res, dy[i])
    print(res)

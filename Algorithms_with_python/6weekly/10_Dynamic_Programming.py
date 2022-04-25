#동전 교환
#냅색 알고리즘과 같음
#dy=[j]: j원을 거슬러주는데 사용된 동전의 최소 갯수

import sys
sys.stdin = open("input10.txt","r")

if __name__ =="__main__":
    n = int (input())
    coin=list(map(int, input().split()))
    m = int(input())
    dy=[1000]*(m+1);
    dy[0]=0

    for i in range(n):
        for j in range(coin[i],m+1):
            dy[j]=min(dy[j],dy[j-coin[i]]+1)

    print(dy[m])

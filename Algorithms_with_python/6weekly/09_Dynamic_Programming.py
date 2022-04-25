#가방문제 (냅색 알고리즘)
#dy[j] : 가방에 j 무게 만큼 담았을때 보석의 최대 가치
import sys
sys.stdin = open("input09.txt","r")


if __name__=="__main__":
    n,m = map(int, input().split())
    dy=[0]*(m+1);
    for i in range(n):
        w, v = map(int,input().split())
        for j in range(w, m+1):
            dy[j] = max(dy[j],dy[j-w]+v)
    print(dy[m])


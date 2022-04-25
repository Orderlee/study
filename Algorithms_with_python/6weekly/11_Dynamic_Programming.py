#최대점수 구하기(냅색 알고리즘)
#한 유형에 하나만 풀 수 있음
# dy[i][j]:  i는 i번쨰 문제까지 적용 j는 주어진 시간
# dy
import sys
sys.stdin = open("input11.txt","r")

if __name__ == '__main__':
    n,m = map(int,input().split())
    dy=[0]*(m+1);
    for i in range(n):
        ps, pt = map(int, input().split())
        for j in range(m,pt-1, -1):
            dy[j] = max(dy[j], dy[j-pt]+ps)
    print(dy[m])

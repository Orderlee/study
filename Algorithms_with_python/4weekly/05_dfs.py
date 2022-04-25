# 합이 같은 부분집합(DFS: 아마존 인터뷰)

import sys
sys.stdin = open("input05.txt","r")

def DFS(L,sum):       #L: a리스트 참조하는 index번호  sum: 부분집합의 누적 합
    if sum>total//2:    # total 값이 홀수라면 no만 나오는데, 원소 합이 6이 나오면 참이 되는걸 방지
        return
    if L==n: #종착지점
        if sum == (total-sum): #선택되지 않은 부분집합
            print("YES")
            sys.exit(0) # 프로그램 전체를 종료시킴
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)



if __name__== "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0,0)
    print("NO")
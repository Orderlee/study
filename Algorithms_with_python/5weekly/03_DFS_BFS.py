#양팔저울(DFS)

import sys
sys.stdin = open("input03.txt","r")

def DFS(L, sum): # L: G를 접근하는 index, sum:측정할 수 있는 물의 무게
    global res # set의 자료 구조
    if L == n:
        if 0 <sum<=s:   #음수는 생각 안해도 됨, 가지치기중 다른 쪽에서 대응하는 양수가 나옴
            res.add(sum) #set 자료구조를 사용하는 이유는 중복되는 값을 피하기 위해서

    else:
        DFS(L+1, sum+G[L]) #추를 왼쪽에 놓는 상황
        DFS(L+1, sum-G[L]) #추를 오른쪽에 놓는 상황
        DFS(L+1, sum) # 추를 사용하지 않겠다.



if __name__ == "__main__":
    n =int(input())
    G=list(map(int, input().split())) #각 추의 무게
    s=sum(G) # 추의 총합
    res = set() #측정 할 수 있는 무게를 추가
    DFS(0,0)
    print(s-len(res)) #s 총 경우의 수 , len(res): 측정하는 무게 총 경우의 수
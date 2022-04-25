#네트워크 선 자르기 #top-down:재귀, 메모이제이션식

import sys

sys.stdin = open("input02.txt","r")

def DFS(len):
    #가지자르기
    if dy[len]>0:
        return dy[len]
    #
    if len == 1 or len ==2:
        return len
    else:
        dy[len]= DFS(len-1) + DFS(len-2)
        return dy[len]







if __name__=="__main__":
    n = int(input())
    dy=[0]*(n+1)
    print(DFS(n))

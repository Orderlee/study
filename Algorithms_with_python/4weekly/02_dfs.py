#이즌트리 순회 (깊이우선탐색)
import sys
sys.stdin = open("input02.txt","r")

def DFS(x):
    if x ==0:
        return
    else:
        #print(x%2, end=' ')
        DFS(x//2)
        print(x % 2, end=' ')


if __name__ =="__main__":
    n = int(input())
    DFS(n)
#이진트리 순회 (깊이우선탐색)
# 출력순서  부모, 왼쪽, 오른쪽 :전위순회
#         왼 ,  부,  오  : 중위순회
#         왼,   오,  부   : 후위순회


import sys

sys.stdin = open("input03.txt","r")


def DFS(x):
    if x>7:
        return
    else:
        #print(x, end=' ') #전위순회 ,순회방식중에서 전위순회를 많이 사용
        DFS(x*2)
        #print(x, end=' ') #중위순회
        DFS(x*2+1)
        print(x, end=' ') #후위순회, 대표적인게 병합정렬




if __name__=="__main__":
    DFS(1)
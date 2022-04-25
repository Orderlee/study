#재귀함수와 스택
# 자기 자신을 호출하는 함수
import sys
sys.stdin = open("input.txt","r")

def DFS(x):
    if x>0:
        #print(x, end=' ')
        DFS(x-1)
        print(x, end=' ') #print를 DFS 위에서 하느냐 아래에서 하느냐 출력 값이 다름 , 재귀가 STACK을 활용함 ,stack 프레임: 값의 매개변수, 지역변수, 복귀 주소
                            #값이 참이면 if문에 있는 DFS 함수로 복귀, 값이 거짓이면 종료, 스택에 마지막에 쌓인 값이 DFS함수에 복귀후 print로 출력, 모든 값을 출력 후  if__name__ =="__main__"으로 복귀


if __name__=="__main__":
    n = int(input())
    DFS(n)
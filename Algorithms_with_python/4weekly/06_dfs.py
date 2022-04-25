#전역변수와 지역변수


def DFS1():
    cnt=3 #dfs1의 지역변수가 됨
    print(cnt) #지역변수
                #지역변수에 없으면 전역변수에서 찾음
                #함수는 지역변수가 전역변수보다 먼저

def DFS2():
    global cnt # cnt는 전역변수다 라고 지정함
    if cnt==5:
        cnt=cnt+1  #global cnt로 인해서 기존 전역변수 값을 사용한다고 해석함 #global cnt 없었으면 지역변수로 사용
        print(cnt)

if __name__ == "__main__":
    cnt=5 #전역변수 #변수를 생성과 값을 할당을 함 , 기본적으로 모든 함수가 전역변수에 접근 가능
    DFS1()
    DFS2()
    print(cnt)



# 리스트에서 작동하는지 확인

def DFS():
    a = a+[4] #오류나는 경우   #로컬리스트를 만들겠다고 인식 a는 할당된 값이 없고 4라는 리스트를 더하기 떄문에 오류
    #a=[7,8] # --> 로컬 리스트
    #a[0]=7 #로컬 리스트가 아님, 전역 리스트임
    print(a)

if __name__ =="__main__":
    a=[1,2,3]
    DFS()
    print(a)
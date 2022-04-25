#수열 추측하기
# itertools 라이브러리에 의존 하지 말것
#
import sys
import itertools as it #itertools 라이브러리가 순열이나 조합을 자동적으로 구해줌
sys.stdin = open("input14.txt","rt")

n, f = map(int, input().split())
b=[1]*n
cnt=0
for i in range(1,n):
    b[i] = b[i-1]*(n-i)/i

a = list(range(1,n+1))
for tmp in it.permutations(a):
#     print(tmp)
#     cnt+=1
# print(cnt)
    sum = 0
    for L, x in enumerate(tmp):
    #     print(L,x)
    # break
        sum+=(x*b[L])
    if sum==f:
        for x in tmp:
            print(x, end=' ')
        break  # for tmp in it.permutations(a): 브레이크 함, 더이상 순열을 만들어 보지 않음


# for tmp in it.permutations(a,3): # a 리스트에서 3개만 뽑아라
#     print(tmp)
#     cnt+=1
# print(cnt)
#이분검색
#결정 알고리즘에서 사용
import sys
sys.stdin = open("input.txt", "r")
n, m =map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n-1
while lt<=rt:
    mid = (lt+rt)//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] >m:
        rt=mid = 1
    else:
        lt = mid+1


print(lt)
print(rt)

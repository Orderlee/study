#교육과정 설계
import sys
from collections import deque
sys.stdin=open("input26.txt","r")
need=input()
n = int(input())
for i in range(n):
    plan=input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x!= dq.popleft():
                print("#%d N0" %(i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))

        else:
            print("#%d, No" %(i+1))




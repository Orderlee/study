#가장 큰 수
# stack 은 last in first out (LIFO)

import sys
sys.stdin=open("input20.txt","rt")
#sys.stdin=open("input20_1.txt","rt")

num, m = map(int, input().split())
num = list(map(int,str(num)))
#print(num)

stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)

if m !=0:
    stack = stack[:-m]


#print(stack)
res = ''.join(map(str,stack))
print(res)

# for x in stack:
#     print(x, end='')

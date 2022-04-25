#쇠막대기
import sys
sys.stdin=open("input21.txt","r")
#sys.stdin=open("input21_1.txt","r")
s = input()
stack=[]
cnt=0

for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] =='(':
            #stack.pop()
            cnt+=len(stack)
        else:
            #stack.pop()
            cnt+=1

print(cnt)
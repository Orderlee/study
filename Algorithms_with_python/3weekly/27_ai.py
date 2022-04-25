#단어 찾기
import sys
sys.stdin = open("input27.txt","r")
n=int(input())
p=dict()
for i in range(n):
    word = input()
    p[word]=1
#print(p)
for i in range(n-1):
    word=input()
    p[word]=0
#print(p)
for key, val in p.items():
    #print(key,val)
    if val==1:
        print(key)
        break
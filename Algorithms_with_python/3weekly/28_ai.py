#아나그램
import sys
sys.stdin= open("input28.txt","r")
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x]=str1.get(x,0)+1
#print(str1)
for x in b:
    str2[x] = str2.get(x,0)+1

for i in str1.keys():
    #print(i)
    if i in str2.keys():
        if str1[i]!=str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break

else:
    print("YES")


#개선코드
sys.stdin=open("input28.txt","r")
a=input()
b=input()
sH=dict()


for x in a:
    sH[x]=sH.get(x,0)+1
for x in b:
    sH[x]=sH.get(x,0)-1

for x in a:
    if sH.get(x)>0:
        print("NO")
        break
else:
    print("YES")


#리스트
sys.stdin=open("input28.txt","r")
a=input()
b=input()
str1=[0]*52
str2=[0]*52

for x in a:
    if x.isupper():
        str1[ord(x)-65]+=1  #ord 문자를 아스키숫자로 변환    #대문자 A~Z 65~90 소문자 a~z 97~122
        #print(ord(x))
    else:
        str1[ord(x)-71]+=1 #소문자는 71를 빼면 25 이후로 순차적입력

for x in b:
    if x.isupper():
        str2[ord(x)-65]+=1
        #print(ord(x))
    else:
        str2[ord(x)-71]+=1

#print(str1)
#print(str2)

for i in range(52):
    if str1[i] !=str2[i]:
        print("NO")
        break
else:
     print("YES")
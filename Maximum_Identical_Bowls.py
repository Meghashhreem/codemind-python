n=int(input())
l=list(map(int,input().split()))
c=len(l)
s=sum(l)
while(c):
    if s%c==0:
        print(c)
        break
    else:
        c-=1
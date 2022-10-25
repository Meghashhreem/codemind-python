n=int(input())
l=list(map(int,input().split()))
e=[]
o=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
if len(e)%2==0 and len(o)%2==0:
    print(1)
else:
    print(0)
n=int(input())
l=[]
c=0
v=0
while n:
    d=n%10
    l.append(d)
    n=n//10
    v+=1
for i in range(v):
    for j in range(v):
        if l[i]==l[j]:
            c+=1
if c==v:
    print("Unique Number")
else:
    print("Not Unique Number")
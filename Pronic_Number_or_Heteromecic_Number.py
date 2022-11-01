n=int(input())
d=0
for i in range(1,n//2):
    if (i*(i+1)==n):
        d+=1
if (d>0):
    print("YES")
else:
    print("NO")
n=int(input())
k=0
for i in range(1,n//2):
    if (i*i==n):
        k+=1
if k==1:
    print("True")
else:
    print("False")
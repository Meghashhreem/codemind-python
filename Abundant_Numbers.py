N=int(input())
s=0
for i in range(1,N):
    if (N%i==0):
        s+=i
if (s>N):
    print("True")
else:
    print("False")

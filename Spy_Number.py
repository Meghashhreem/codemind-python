N=int(input())
sum1=0
prod=1
num1=N
while N>0:
    k=N%10
    sum1=sum1+k
    prod=prod*k
    N=N//10
if (sum1==prod):
    print("Spy Number")
else:
    print("Not Spy Number")
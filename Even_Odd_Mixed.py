n=int(input())
c=0
cc=0
while n>0:
    r=n%10
    if r%2==0:
        c+=1
    else:
        cc+=1
    n=n//10
if c==0:
    print("Odd")
elif cc==0:
    print("Even")
else:
    print("Mixed")
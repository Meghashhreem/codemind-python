def isprime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
n=int(input())
if isprime(n):
    c=0
    p=0
    while(n):
        r=n%10
        n=n//10
        c+=1
        if(isprime(r)):
            p+=1
    if p==c:
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')

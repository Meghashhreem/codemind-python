from math import sqrt
def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            fc=0
            for j in range(1,n+1):
                if i%j==0:
                    fc+=1
            if fc!=2:
                c+=1
    return c
n=int(input())
print(prime(n))
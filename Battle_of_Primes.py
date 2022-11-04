def prime(s1):
    for j in range(2,int(s1**0.5)+1):
        if s1%j==0:
            return 0
    else:
        return 1
def fun(s):
    for i in range(1,11):
        s1=s+i
        if prime(s1):
            return i
n=int(input())
m=int(input())
s=m+n
print(fun(s))
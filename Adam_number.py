n=int(input())
sqr=n*n
rev=0
temp=sqr
while n:
    r=n%10
    n=n//10
    rev=rev*10+r
rev1=rev*rev
a=0
while rev1:
    b=rev1%10
    rev1=rev1//10
    a=a*10+b
if (sqr==a):
    print("True")
else:
    print("False")
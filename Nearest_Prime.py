t=int(input())
while(t):
    k=0
    m=0
    a=[]
    b=[]
    n=int(input())
    for i in range(0,n+100):
        c=2
        for j in range(2,i):
            if i%j==0:
                c+=1
        if c==2:
            a.append(abs(n-i))
            b.append(i)
            m+=1
    d=a[0]
    for i in range(0,m):
        if d>a[i]:
            d=a[i]
            p=b[i]
    print(p)
    t-=1
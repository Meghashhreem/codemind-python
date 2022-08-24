t=int(input())
lst=[]
for i in range(t):
    n=input()
    val=n.split()
    lst.append(val)
for i in lst:
    L=int(i[0])
    R=int(i[1])
    arr=[j for j in range(L,R+1)]
    cnt=0
    for k in arr:
        val=str(k)
        if (val[-1]=='2') or (val[-1]=='3') or (val[-1]=='9'):
            cnt+=1
    print(cnt)
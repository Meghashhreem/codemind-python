a,b=map(int,input().split())
if(a==1 and b==2 or a==2 and b==3 or a==3 and b==4 or a==4 and b==5 or a==5 and b==6 or a==6 and b==7 or a==7 and b==8 or a==8 and b==9 or a==9 and b==10 or a==10 and b==1):
    print('Yes')
elif(b==1 and a==2 or b==2 and a==3 or b==3 and a==4 or b==4 and a==5 or b==5 and a==6 or b==6 and a==7 or b==7 and a==8 or b==8 and a==9 or b==9 and a==10 or b==10 and a==1):
    print('Yes')
else:
    print('No')

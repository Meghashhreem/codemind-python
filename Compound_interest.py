import math
p,r,t=map(int,input().split())
A=p*(pow((1+r/100),t))
print("{:.2f}".format(A))
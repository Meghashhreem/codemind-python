x,y=map(int,input().split())
if x > y:
  x, y = y, x
for i in range(1,x+1):
  if x%i == 0 and y%i == 0:
    gcd = i

lcm = (x*y)//gcd

print(lcm)
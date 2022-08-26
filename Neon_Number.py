num = int(input())
sqr = num*num 
sum1 = 0
while sqr>0:
    sum1 =sum1 + sqr%10
    sqr = sqr//10
if (num == sum1):
    print("Neon Number")
else:
    print("Not Neon Number")
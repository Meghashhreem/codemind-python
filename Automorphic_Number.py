n=int(input())
num_of_digits=len(str(n))
sqr=n*n
last_digit=sqr%pow(10,num_of_digits)
if (last_digit==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

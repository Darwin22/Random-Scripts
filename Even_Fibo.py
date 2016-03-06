s=0
evens =2
x,y =1,2
n = input("Enter the limit: ")
while (x+y) < int(n):
   s = x+y
   x=y
   y= s
   if s%2 == 0:
      evens+=s
print (evens)

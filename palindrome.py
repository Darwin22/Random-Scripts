def palin(n):
     p=n
     s=0
     while n!=0:
          n = n%10
          s = s+n*10
          n =n/10

     if n==p:
          print('%d is a palin' % n)
     else:
          print('%d  is not palin' % n)

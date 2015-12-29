#num = input('Enter how many do you want: ')

# fibona(num)
'''def fibona(n):
     'Calculate fibonacci series.'
     a, b = 0,1
     #a = [0,1]
     #for i in range(n-2):
     for i in range(n):
          #a.append(a[-2] + a[-1])
          a, b = b, a + b
          #print a
     return a '''


# Recursive Fibonacci

''' def fab(n, first=0, second =1):
     if n==1:
          return [first]
     else:
          return [first] + fab(n-1, second, first+second) '''


# OR
n = input("How many numbers do you need: ")
fibs = [0,1]
for i in range(n-2):
     fibs.append(fibs[-2] + fibs[-1])
for p in fibs:
    print p

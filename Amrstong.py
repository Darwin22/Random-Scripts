#!/usr/bin/env python
# TO check a number is an armstrong number
n = input('Enter a number to check its armstrong: ')
p=n
su=0
while n != 0:
  a = n%10
  a**3
  su += a
  n = n/10
if(su == p):
   print('Its armstrong')
else:
   print('Its not an armstrong number')





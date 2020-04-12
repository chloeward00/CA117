#!/usr/bin/env python

def range(s):

   multiplesof3 = []
   for n in s:
       if s % 3 == 0:
            multiplesof3.append(s)
            print ('Multiples of 3:' , multiplesof3)

   multiplesof3squared = []
   for n in s:
        if s % 3 == 0:
            multiplesof3squared.append(s**2)
            print ('Multiples of 3 squared:', multiplesof3squared)

   multiplesof4doubled = []
   for n in s:
        if s % 4 == 0:
            multiplesof4doubled.append(s*2)
            print ('Multiples of 4 doubled:', multiplesof4doubled)

   multiplesof3or4 = []
   for n in s:
        if s % 3 == 0 or s % 4 == 0:
            multiplesof3or4.append(s)
            print ('Multiples of 3 or 4:', multiplesof3or4)

   multiplesof3andfour = []
   for n in s:
        if s % 3 == 0 and s % 4 == 0:
            multiplesof3andfour.append(s)
            print ('Multiples of 3 and 4:', multiplesof3andfour)

   multiplesof3replaced = []
   for n in s:
        if s % 3 == 0:
            multiplesof3replaced.append(s)
            s.replace(s, 'X')
            print ('Multiples of 3 replaced:' , multiplesof3replaced)

   primes = []
   for n in s:
        if s % 1 == 0:
            primes.append(s)
            print ('Primes:', primes)

#!/usr/bin/env python

count = 0

import sys
err = []
for lines in sys.stdin:

   i = 0
   total = 0
   string = lines.strip().split()

   try:
      sumofdigits = int(string[0])

      base = int(string[-1])
      while base ** i < sumofdigits:
         i = i + 1
      i -= 1
      count += 1
      formula = []
      while i >= 0:
         n = 0

         while ((base ** i) * n) <= sumofdigits:
            n = n + 1
         n -= 1
         formula.append(int(n))
         sumofdigits = sumofdigits - ((base ** i) * n)
         i -= 1
      for value in formula:
         total = total + (value ** 2)
      print(total)

   except ValueError:
      count += 1
      err.append(str(count) + ",")

if len(err) > 0:
   print('Failed to convert line(s):', " ".join(err)[:-1] + " ")

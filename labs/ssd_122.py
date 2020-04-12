#!/usr/bin/env python

import sys

for lines in sys.stdin:
   total = 0
   string = lines.strip().split()

   sumofdigits = int(string[0])

   base = int(string[-1])

   i = 0
   while base ** i < sumofdigits:
      i = i + 1
   i -= 1

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
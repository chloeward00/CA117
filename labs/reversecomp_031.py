#!/usr/bin/env python

import sys


mylist = []
for lines in sys.stdin:

	words = lines.strip()
	lowerwords = words.lower()
	mylist.append(lowerwords)

print([ s for s in mylist if len(s) >= 5 and s[::-1] in mylist])
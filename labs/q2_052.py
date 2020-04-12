#!/usr/bin/env python

import sys

vowels = ['a', 'e', 'i', 'o', 'u']
found = []
for lines in sys.stdin:
    words = lines.strip().casefold()
    found = [s for s in words if s in vowels]
    if vowels == found:
        print(lines.strip())

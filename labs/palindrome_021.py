#!/usr/bin/env python

import sys
def reverse(s):
    s = s[::-1]
    return s

def palindrome(s):
    rev = reverse(s)
    if s == rev:
        return True
    else:
        return False

lines = sys.stdin.readlines()
for line in lines:
    line = line.lower()
    line = line.strip()
    j = 0
    while j < len(line):
        if not("a" < line[j] < "z" or "A" < line[j] < "Z"):
            line = line.replace(line[j], '')
        j += 1
    print(palindrome(line))

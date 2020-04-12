#!/usr/bin/env python

import sys

lines = sys.stdin.readlines()
for line in lines:
    word1 = line.split()[0]
    word2 = line.split()[1]
    if sorted(word1) == sorted(word2):
        print("True")
    else:
        print("False")

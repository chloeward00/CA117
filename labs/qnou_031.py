#!/usr/bin/env python

import sys

rightlist= ['q']
wronglist = ['qu']

def qnou(s):
    line = sys.stdin.read()
    lines = line.strip().split()
    newline = line.lower()

    for s in s in newline:
        if s in rightlist:
            print("Words with q but no u: {}".format())
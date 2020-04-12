#!/usr/bin/env python

import sys

def diamond(s):
    i = 1
    while i < s + 1:
        stars = (' ' * ( s - i) + '* ' * i).rstrip()
        print (stars)
        i = i + 1
    i = i - 2

    while i > 0:
        stars = (' ' * (s - i) + '* ' * i).rstrip()
        print (stars)
        i = i - 1

def main():
    x = int(sys.argv[1])
    diamond(x)

if __name__ == '__main__':
    main()

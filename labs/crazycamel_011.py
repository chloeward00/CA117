#!/usr/bin/env python

import sys

def caps(s):
    line  = s[::-1].title()
    reverse = line[::-1]
    return reverse

def main():
    for line in sys.stdin:
        if len(line.strip()) > 1:
            capitals = caps(line.strip())
            print (capitals)


if __name__ == '__main__':
    main()
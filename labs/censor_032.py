#!/usr/bin/env python

import sys

def main():
    with open(sys.argv[1], 'r') as f:
        badwords = f.read().strip().split()

    for thelines in sys.stdin:
        thelines = thelines.strip()
        for i in range(len(badwords)):
            if badwords[i] in thelines:
                thelines = thelines.replace(badwords[i], '@' * len(badwords[i]))
        print(thelines)

if __name__ == '__main__':
    main()

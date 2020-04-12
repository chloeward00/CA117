#!/usr/bin/env python

import sys

def emails(s):
     line = s[:-12]
     for x in line:
        if x.isdigit():
            line = line[:-1]
     dot = line.split('.')
     capital = dot[0].title()
     return capital + " " + dot[-1].title()



def main():
    for line in sys.stdin:
        if len(line.strip()) > 1:
            names = emails(line.strip())
            print (names)

if __name__ == '__main__':
    main()
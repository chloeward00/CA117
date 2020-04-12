#!/usr/bin/env python

import sys

def middle(s):
    d = len(s) // 2
    return s[d]

def main():
    for line in sys.stdin:
        letter = middle(line.strip())  
        if len(line.strip()) % 2 == 0:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
            print ('No middle character!')
        else:
            print (letter)

if __name__ == '__main__':
    main()
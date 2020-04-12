#!/usr/bin/env python

import sys

def main():

    dictionary = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
    for line in sys.stdin:
        line = line.strip().split()
        li = []
        translate = [dictionary[int(digit)] for digit in line]
        print(" ".join(translate))

if __name__ == '__main__':
    main()

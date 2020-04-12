#!/usr/bin/env python

import sys

def caps(s):
	first = s[0].upper()
	line  = s[1:-1]
	last  = s[-1].upper()
	return first + line + last

def main():
    for line in sys.stdin:
    	if len(line.strip()) > 1:
    	    capital = caps(line.strip())
    	    print (capital)


if __name__ == '__main__':
	main()
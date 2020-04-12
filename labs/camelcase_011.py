#!/usr/bin/env python

import sys

def caps(s):
	line  = s[0:].title()
	return line

def main():
    for line in sys.stdin:
    	if len(line.strip()) > 0:
    	    capital = caps(line.strip())
    	    print (capital)


if __name__ == '__main__':
	main()
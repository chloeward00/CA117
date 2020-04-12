#!/usr/bin/env python

import sys

def number(s):
	newnumber = s.strip().split()[0]
	base = s.strip().split()[1]
	decimal = int(newnumber, int(base))
	return decimal

def main():
	for line in sys.stdin:
		decimalnumber = number(line.strip())
		print (decimalnumber)

if __name__ == '__main__':
	main()
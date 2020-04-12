#!/usr/bin/env python

import sys

def sub(s):
	f = s.split()
	return f[0].lower() in f[1].lower()

def main():
	for line in sys.stdin:
		print(sub(line))

if __name__ == '__main__':
	main()
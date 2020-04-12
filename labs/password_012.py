#!/usr/bin/env python

import sys

def password_security(s):
	num = 0
	upper = 0
	lower = 0
	special = 0

	i = 0
	while i < len(s):
		if s[i].isdigit():
			num = 1
		elif s[i].islower():
			lower = 1
		elif s[i].isupper():
			upper = 1
		else:
			special = 1
		i = i + 1
	return num + upper + lower + special 

def main():

	for line in sys.stdin:
		security = password_security(line.strip())
		print (security)

if __name__ == '__main__':
	main()
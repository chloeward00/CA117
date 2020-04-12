#!/usr/bin/env python

import sys

 
endings = ['ch', 'h', 'x', 's' , 'z']
consonants = ['b', 'c', 'd', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w' , 'x', 'y', 'z']
vowels = [ 'a', 'i', 'o', 'u']
f = ['f', 'fe']

def noun(s):
    for chars in s:
        if s[-2:] in endings or s[-1] in endings:
            return s + 'es'
        elif s[-1] in vowels:
            return s + 'es' 
        elif s[-2:] == 'fe' or s[-1] == 'f':
            s = s.rstrip('fe')
            return s + 'ves'
        elif s[-2] in consonants and s[-1] == 'y':
            s = s.replace(s[-1], 'ies', 1)
            return s
        else:
            return s + 's'

def main():

    for line in sys.stdin:
        plural = noun(line.strip())
        print (plural)



if __name__ == '__main__':
    main()
#!/usr/bin/env python

import sys

def token(s):

    lines = s.replace('.', ' ')
    newlines = lines.replace(',', ' ')
    nospaces = newlines.replace('  ', ' ')
    justwords = nospaces.replace('--', ' ')
    justwords = justwords.lower()
    return justwords

def main():
    li = []
    for line in sys.stdin:
            names = token(line.strip())
            s = names.split()
            for word in s:
                if word not in li:
                    li.append(word)
    print(len(li))

if __name__ == '__main__':
    main()

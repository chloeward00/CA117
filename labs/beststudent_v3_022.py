#!/usr/bin/env python3

import sys


def main():
    try:
        file = sys.argv[1]
        highestmark = 0
        with open(file, 'r') as f:
            for line in f:
                try:
                    if highestmark < int(line[:2]):
                        highestmark = int(line[:2])
                        bestline = line.strip()
                except ValueError:
                    print('Invalid mark {} encountered. Skipping.'.format(line[:2]))
        bestofmark = bestline[:2]
        beststudentmark = bestline[3:]
        print('Best student: {}'.format(beststudentmark))
        print('Best mark: {}'.format(bestofmark))
    except FileNotFoundError:
        print('The file {} could not be opened.'.format(filename))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        nums = line.strip()
        try:
            print ("Thank you for {}".format(int(nums)))
            return 1

        except ValueError:
            print ("{} is not a number".format(nums))
if __name__ == "__main__":
    main()

#!/usr/bin/env python

import sys

def wordcomps():
    line = sys.stdin.read()
    line = line.strip().split()
    print("Words containing 17 letters: {}".format([s for s in line if len(s) == 17]))
    print("Words containing 18+ letters: {}".format([s for s in line if len(s) > 17]))
    all_vowels = [s for s in line if s.lower().count("a") > 0 and s.lower().count("e") > 0 and s.lower().count("i") > 0 and s.lower().count("o") > 0 and s.lower().count("u") > 0]
    print("Shortest word containing all vowels: {}".format(min(all_vowels, key=len)))
    print("Words with 4 a's: {}".format([s for s in line if s.lower().count("a") == 4]))
    print("Words with 2+ q's: {}".format([s for s in line if s.lower().count("q") > 1]))
    print("Words containing cie: {}".format([s for s in line if "cie" in s]))
    print("Anagrams of angle: {}".format([s for s in line if s.lower() != "angle" and s.lower().count("a") == 1 and s.lower().count("e") == 1 and s.lower().count("n") == 1 and s.lower().count("g") == 1 and s.lower().count("l") == 1 and len(s) == 5]))
    print("Words ending in iary: {}".format(len([s for s in line if s[-4:] == "iary"])))
    count = 0
    for word in line:
        counting = word.lower().count("e")
        if word.lower().count("e") > count:
            count = counting
    print("Words with most e's: {}".format([s for s in line if s.lower().count("e") == count]))

wordcomps()

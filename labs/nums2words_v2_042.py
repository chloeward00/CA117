import sys
dictionary = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
}
for lines in sys.stdin:
    lines = lines.strip().split()
    the_words = []
    for number in lines:
        try:
            the_words.append(dictionary[int(number)])
        except (ValueError, KeyError):
            the_words.append("unknown")
    print (" ".join(the_words))

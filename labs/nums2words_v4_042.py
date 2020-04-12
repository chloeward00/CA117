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
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one hundred",
}

for lines in sys.stdin:
    lines = lines.split()

    the_words = []
    for number in lines:
        if len(number) == 2 and int(number) > 19 and int(number) % 10 != 0:
            the_words.append(dictionary[int(number[0]) * 10] + "-" + dictionary[int(number[1])])
        else:
            the_words.append(dictionary[int(number)])

    print (" ".join(the_words))

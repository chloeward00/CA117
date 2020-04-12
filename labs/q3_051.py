import sys

lowerwords = []

for lines in sys.stdin:
    letters = lines.strip()
    lowerwords = [ch for ch in letters if ch >= "a" and ch <= "z"]
    for c in letters:
        if c in lowerwords:
            letters = letters.replace(c, ' ')
    letters = letters.strip().split()
    print(max(letters, key=len))

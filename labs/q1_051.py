import sys


def main():
    word = sys.argv[1]
    characters = [s for s in word]
    for i in range(0, len(characters), 2):
        try:
            tmp = characters[i]
            characters[i] = characters[i + 1]
            characters[i + 1] = tmp
        except IndexError:
            pass
    print(''.join(characters))


if __name__ == '__main__':
    main()

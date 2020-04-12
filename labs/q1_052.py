import sys

def main():
    d = []
    for theletters in sys.argv[1]:
        theletters.strip().split()
        d.append(theletters)
    i = 0
    j = 1
    while j < len(d):
        tmp = d[i]
        d[i] = d[j]
        d[j] = tmp
        i = i + 2
        j = j + 2

    theword = ""
    i = 0
    while i < len(d):
        theword = theword + d[i]
        i = i + 1
    print(theword)

if __name__ == '__main__':
    main()

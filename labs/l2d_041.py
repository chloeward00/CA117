def l2d(file):
    dictionary = {}
    thekeys = file.readline().strip().split()
    thevalues = file.readline().strip().split()
    for k, v in zip(thekeys, thevalues):
        dictionary[k] = int(v)
    return dictionary

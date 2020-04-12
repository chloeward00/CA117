def minimum(s):

    if len(s) == 1:
        return s[0]

    if s[0] <= minimum(s[1:]):
        return s[0]
    else:
        return minimum(s[1:])

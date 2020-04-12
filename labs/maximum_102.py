def maximum(s):

    if len(s) == 1:
        return s[0]

    if s[0] >= maximum(s[1:]):
        return s[0]
    else:
        return maximum(s[1:])

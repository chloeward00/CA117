def reverse_list(s):
    if len(s) == 1:
        return s
    elif len(s) == 0:
        return s

    return reverse_list(s[1:]) + [s[0]]

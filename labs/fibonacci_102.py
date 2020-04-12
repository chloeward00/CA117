def fibonacci(s):
    if s == 0 or s == 1:
        return 1

    return fibonacci(s - 1) + fibonacci(s - 2)

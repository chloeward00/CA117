
from stack_092 import Stack
from math import sqrt

def calculator(line):
    line = line.strip().split()
    op = ["+", "-", "/", "r", "n", "*"]
    if len(line) == 1:
        return float(line[0])
    stack = Stack()
    operation = []
    for b in line:
        num = 0
        if set(b).issubset(("0123456789.")):
            stack.push(float(b))
        else:
            operation.append(b)

    i = 0
    while i < len(operation):
        if operation[i] == "+":
            s = stack.pop()
            t = stack.pop()
            stack.push((s + t))
        elif operation[i] == "-":
            s = stack.pop()
            t = stack.pop()
            stack.push((t - s))
        elif operation[i] == "/":
            s = stack.pop()
            t = stack.pop()
            stack.push((t / s))
        elif operation[i] == "n":
            s = stack.pop()
            stack.push(-1 * s)
        elif operation[i] == "r":
            s = stack.pop()
            stack.push(sqrt(s))
        elif operation[i] == "*":
            s = stack.pop()
            t = stack.pop()
            stack.push((s * t))
        i += 1

    return stack.pop()

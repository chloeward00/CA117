from stack_092 import Stack

def matcher(line):

    s = Stack()

    lefties = '({['
    righties = ')}]'
    brackets = ['()', '{}', '[]']
    line = line.strip()

    try:
        for pattern in line:
            if pattern in lefties:
                s.push(pattern)
            else:
                if s.top() + pattern in brackets:
                    s.pop()
        return s.is_empty()
    except:
        return False

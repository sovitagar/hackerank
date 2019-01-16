# Enter your code here. Read input from STDIN. Print output to STDOUT


# Enter your code here. Read input from STDIN. Print output to STDOUT

def characters(exp, pairs = {'[': ']', '{': '}', '(': ')'}):

    strval = ""
    for i in range(len(exp)):
        if exp[i] in ('(',')','{','}','[',']'):
            strval = strval+exp[i]

    opening = pairs.keys()
    closing = pairs.values()
    match = list()
    for s in exp:
        if s in opening:
            match.insert(0, s)
        elif s in closing:
            if len(match) == 0:
                return 'N' + ' ' + strval
            if match[0] == opening[closing.index(s)]:
                match.pop(0)
            else:
                return 'N' + ' ' + strval

    if len(match) == 0:
        return 'Y' + ' ' + strval

    return 'N' + ' ' + strval




if __name__ == "__main__":
    expression=raw_input()
    value = characters(expression)
    print(value)



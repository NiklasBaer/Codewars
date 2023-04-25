def rotate(s):
    if len(s) == 0:
        return []
    output = []
    x = list(s)
    for i in range(len(s)):
        y = x.pop(0)
        x.append(y)
        xstring = "".join(x)
        t = output.append(xstring)
    return output

        










rotate("Hello")
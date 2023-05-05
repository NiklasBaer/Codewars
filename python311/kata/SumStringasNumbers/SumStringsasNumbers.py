def sum_strings(x, y):
    if x == "" and y == "":
        return "0"
    if x == "":
        return y
    elif y == "":
        return x
    print(x, y)

    Ergbenis = int(x) + int(y)
    return str(Ergbenis)


sum_strings("1", "1")

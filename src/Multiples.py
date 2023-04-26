def multiple(x):
    if int(x) % 3 == 0 and int(x) % 5 == 0:
        return "BangBoom"
    
    elif int(x) % 3 == 0:
        return "Bang"
    elif int(x) % 5 == 0:
        return "Boom"
    else:
        return "Miss"

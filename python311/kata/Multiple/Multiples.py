def multiple(x):
    if x == []:
        return []
    elif int(x )<= 0 :
        return "Miss"
    if int(x) % 3 == 0 and int(x) % 5 == 0:
        return "BangBoom"
    
    elif int(x) % 3 == 0:
        return "Bang"
    elif int(x) % 5 == 0:
        return "Boom"
    else:
        return "Miss"

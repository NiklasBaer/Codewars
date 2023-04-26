def evaluate(equation):
    equation = equation
    testeq = list(equation)
    nutzlos = testeq.pop()
    Prüfen = testeq.pop()
    modeq = "".join(equation.split()) #1@1
    ls = list(equation)
    if Prüfen == "-":
        a = ls.pop()
        a = ls.pop()+  a 
    print(a)
    b = ls.pop()
    a = int(a)
    b = int(b)
    if b == 0:
        return
    
    Ergebnis = (a+b)+(a-b)+(a*b)+(a//b)
    return Ergebnis
    
#valuate("1 @ 1")
#evaluate('3 @ 2')
evaluate("1 @ 1 @ -4")
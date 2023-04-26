def evaluate(equation):
    equation = equation
    x = "".join(equation.split())
    moded_lis = x.replace("@", "")
    ls1 = list(moded_lis)
    
    A = ls1.pop(0)
    B = ls1.pop(0)
    if A == "-":
        print("Test")
        A = "-" + ls1.pop(0)
        
    if B == "-":
        print("Test2")
        B = "-" + ls1.pop(0)
    
    print(A, B)
    print(ls1)
    
evaluate("-1 @ -1 @ 1")
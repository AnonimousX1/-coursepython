print ("Extração de Raizes")
a= float(input("Qual o valor do quoficiente a?: "))
b= float(input("Qual o valor de quoficiente b?: "))
c= float(input("Qual o valor de quoficiente c?: "))
delta = b**2-4*a*c
if delta > 0:
    x = (-b+(delta**0.5))/(2*a)
    x2= (-b-(delta**0.5))/(2*a)
    if x2<x:
        print("as raízes da equação são", x2, "e", x)
    elif x>x2:
        print("as raízes da equação são", x, "e", x2)
elif delta == 0:
    x = (-b+(delta**0.5))/(2*a)
    print("a raiz desta equação é",x)
else:
    print("esta equação não possui raízes reais")

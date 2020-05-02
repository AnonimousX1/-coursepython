x1 = float(input("Digite o numero da 1º coordenada x número: "))
y1 = float(input("Digite o numero da 1º coordenada y número: "))
x2 = float(input("Digite o numero da 2º coordenada x número: "))
y2 = float(input("Digite o numero da 2º coordenada y número: "))
d=(((x2-x1)**2)+((y2-y1)**2))**0.5
print(d)
if d >= 10:
    print("longe")
else:
    print("perto")

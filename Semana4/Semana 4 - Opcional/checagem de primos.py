n = int(input("Digite um numero inteiro: "))
divisor = 2
condicao = True
while divisor < n and condicao:
    if n%divisor == 0: 
        condicao = False
    divisor=divisor+1
if n%divisor == 0:
    print("primo")
else:
    print("não primo")

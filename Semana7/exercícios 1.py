a = int(input("Digite um número para o fatorial: "))
while a>0:
    count = 1
    resultado = 1
    while count <= a:
        resultado = resultado*count
        count = count+1
    a = a-a
print(resultado)
 

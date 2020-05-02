def funcao(a):
    count = 1
    resultado = 1
    while count <= a:
        resultado = resultado*count
        count = count+1
    return resultado

b =int(input("Digite um número inteiro positivo: "))
print (funcao(b))



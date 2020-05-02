meucartao = int(input("Digite o seu numero de cartão de crédito: "))
cartão = 1
while meucartao !=cartão:
    cartão = int(input("Digite o número do próximo cartão: "))
    if meucartao == cartão:
        cartão=meucartao
        print("Meu cartão na lista")
    if cartão == 0:
        cartão = meucartao
        print("Meu cartão não está na lista")

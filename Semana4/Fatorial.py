def main():
    '''
    Programa que lê um número inteiro n >= 0 e imprime n!
    '''
    # leia o valor de n
    n = int(input("Digite um número inteiro não-negativo: "))

    # inicializações
    i  = 1  # contador
    n_fat = 1  

    # calcule n!
    while n >= i:
        n_fat = n_fat * i 
        i = i + 1

    print(n_fat)
main()

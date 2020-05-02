def primo(n):
    divisor = 2
    condicao = True
    while divisor < n and condicao:
        if n%divisor == 0: 
            condicao = False
        divisor=divisor+1
    return condicao

def maior_primo(n):
    condicao = primo(n)
    while (condicao == False):
        n = n-1
        condicao=primo(n)
    return n

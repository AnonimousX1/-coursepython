def fatorial(n):
    count =1
    fator = 1
    while n >= count:
        fator = fator*count
        count = count+1
    return fator

def binomial(n,k):
    calculo = fatorial(n)/(fatorial(k)*fatorial(n-k))
    return calculo

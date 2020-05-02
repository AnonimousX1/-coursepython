# função principal para combinação
def combinacao(m,n):
    '''
    Este comando serve para fazer o calculo de combinações binomiais
    '''
    #corpo do comando de combinação
    return fatorial(m)/(fatorial(m-n)*fatorial(n))
#função da fatoração
def fatorial(k):
    '''
    Este comando usa comandos whiles para reproduzir um calculo fatorial
    '''
    #corpo do comando fatorial
    fator = 1
    k_fat = 1
    while k >= fator:
        k_fat= k_fat*fator
        fator= fator+1
    return k_fat
#função das espansões binomiais
def coeficiente(x,y,n):
    '''
    Este comando executa o cálculo das expansões binomiais
    '''
    #corpo do comando expansão binomial
    return ((x+y)**n)

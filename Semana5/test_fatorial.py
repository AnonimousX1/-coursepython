def fatorial(n):
    count = 1
    fator = 1
    while n >= count:
        fator = fator*count
        count = count+1
        if n<= 0:
            fator = 1
    return fator

def test_fatorial0():
    assert fatorial(0)==1
def test_fatorial1():
    assert fatorial(1)==1
def test_fatorial2():
    assert fatorial(2)==2
def test_fatorial3():
    assert fatorial(3)==6
def test_fatorial4():
    assert fatorial(4)==24
def test_fatorial_negativo():
    assert fatorial(-10)==1

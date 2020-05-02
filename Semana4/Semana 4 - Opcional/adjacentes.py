num = int(input("Informe um número inteiro: "))
adj = "não"
dig_a = num % 10

while (num > 0):
    num //= 10
    dig_b = num % 10
    if (dig_a == dig_b):
        adj = "sim"
    dig_a = dig_b

print(adj)

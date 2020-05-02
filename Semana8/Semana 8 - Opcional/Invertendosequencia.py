z = []
n=1
while n>0:
    n = int(input("Digite um número: "))
    z.append(n)
    if n == 0:
        del z[-1]
        z.reverse()
for i in z:
    print(i)

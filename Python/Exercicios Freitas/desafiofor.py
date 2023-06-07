qtdd = int(input("Quantas notas voçê quer digitar?: "))
soma = 0
for x in range(0, qtdd, 1):
    soma = soma + float(input("Digite uma nota: "))
print(soma/qtdd)

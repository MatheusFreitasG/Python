peso = float(input("Coloque aqui seu peso: "))
altura = float(input("Coloque aqui seu peso: "))
imc = peso/(altura*altura)

if imc < 18.5:
    print("Você esta abaixo do peso normal")
elif imc >= 18.5 and  imc < 25:
    print("Você esta com o peso normal")
elif imc >= 25 and imc < 30:
    print("Você esta com excesso de peso")
elif imc >= 30 and imc < 35:
    print("Você esta com obesidade classe 1")
elif imc >= 35  and imc< 40:
    print("Você esta com obesidade classe 2")
elif imc > 40:
    print("Você esta com obesidade classe 3")
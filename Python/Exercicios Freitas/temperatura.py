temperatura = float(input("Coloque quantos graus está: "))
if temperatura >= 30 and temperatura <= 40:
    print("Leve água gelada")
elif temperatura >= 20 and temperatura <= 29:
    print("O clima esta ameno")
elif temperatura < 20:
    print("Leve blusa")
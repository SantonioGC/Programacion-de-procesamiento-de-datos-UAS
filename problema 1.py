num = int(input("Ingrese calificación: "))

if 0<= num < 5:
    print("SUSPENSO")
elif 5 <= num < 6:
    print("SUFICIENTE")
elif 6 <= num < 7:
    print("BIEN")
elif 7 <= num < 9:
    print("NOTABLE")
elif 9 <= num <= 10:
    print("SOBRESALIENTE")
else:
    print("NOTA NO VÁLIDA")
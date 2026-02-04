def cont_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0

    for char in cadena:
        if char in vocales:
            contador += 1

    return contador

cadena_test = input("Ingrese una cadena de texto: ")
num_vocales = cont_vocales(cadena_test)

print(f"numero de vocales en la cadena: {num_vocales}")
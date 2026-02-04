def sumar_dos(a, b):
    return a + b

numeros = [10, 5, 8, 12, 3, 7, 15]
resultado = 0

for n in numeros:
    resultado = sumar_dos(resultado, n)

print(f"la suma total de los siete numeros es: {resultado}")

"""Ejercicio N.5
Programa para calcular la cantidad de digitos de un número"""

print("---------------------------------------")
print("---------CANTIDAD DE DIGITOS --------------")
print("---------------------------------------")

# input

A=int(input("Ingrese el número: "))

# processing

Z=int(len(str(A)))

# output

print(str(A) + " tiene " + str(Z) + " digitos.")
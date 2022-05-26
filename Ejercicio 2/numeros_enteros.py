"""Ejercicio 2 
Programa que dado un rango de números enteros, obtenga la
cantidad de números que contiene"""

print("------------------------------------------")
print("-------Cantidad numeros en  un rango -------")
print("------------------------------------------")

#input

A=int(input("ingrese el primer número del rango: "))
B=int(input("ingrese el último número del rango: "))


#processing and output

if A<B:
    C_N=0
    A=A+1
    while A<B:
     A=A+1
     C_N= C_N+1
     print("La cantidad de números del rango es: ", C_N) 
else:
    print("El primer numero del rango es mas grande que el segundo")
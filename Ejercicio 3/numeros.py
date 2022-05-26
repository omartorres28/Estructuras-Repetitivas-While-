"""Ejercicio 3
Programa que dado un rango de números enteros 
obtiene la cantidad de números pares que contiene"""

print("-----------------------------------------------")
print("---------- Cntidad de numers pares ----------")
print("-----------------------------------------------")

# input 
A=int(input("ingrese el valor de A: "))
B=int(input("ingrese el valor de B: "))

# processing
if A<B:
    C_N=0
    A=A+1
    while A<B:
        R=A%2
        if(R==0):
            C_N=C_N+1
        A=A+1
    print("La cantidad de números pares es: " +str(C_N))

else:
    print("El primer numero del rango es mas grande que el segundo")
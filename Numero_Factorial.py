# -*- coding: utf-8 -*-
#Código creado como ejemplo por Patricio Riffo para ámbitos de estudios...
#Este código puede ser utilizado para determinar el factorial de un numero.

#Opcion 1: Funcion Recursiva que calcula un numero factorial
def factorial(n): #Funcion Recursiva que nos retorna el valor de un numero factorial
    if n == 1:    #Si llegamos hasta 1, retornamos 1 para que se comience la multiplicacion
        return 1
    else:
        return n * factorial(n-1)  #Retornamos el valor actual multiplicado por este menos la unidad


def factorial_2(m):
    valor = 1
    for x in range(1,m+1): #recorremos desde 1 hasta m+1, para realizar las multiplicaciones correspondientes
        valor = valor * x  #Multiplicamos la variable valor por los elementos que nos entrega el ciclo for
    return valor           #retornamos el resultado obtenido
        
a=factorial(5) #hacemos el llamado a la funcion recursiva y guardamos el valor en la variable a
print "Al utilizar la funcion recursiva:",a

b=factorial_2(5) #hacemos el llamado a la funcion no recursiva y guardamos el valor en la variable b
print "Al utilizar la funcion No recursiva:",b
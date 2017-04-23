# -*- coding: utf-8 -*-
#Código creado como ejemplo por Patricio Riffo para ámbitos de estudios.
#Este código puede ser utilizado cuando se desea elegir de manera aleatoria a una persona para una determinada tarea o labor.
#Cabe recordar que los números obtenidos son 'pseudoaleatoreos' ya que son obtenidos a traves de formulas matemáticas.

import random as ra #Importamos la librería  que nos permite utilizar números randomicos y la llamaremos "ra".

nombres          = ["Juan","Rene","Carlos","Alex","Andres","Diego"] #Lista con nombres.
cantidad_nombres = len(nombres) #Obtenemos la cantidad de números en el arreglo.
aleatorio        = ra.randrange(cantidad_nombres) #Solicitaremos un N° aleatorio entre 0 y la cantidad de elementos presentes en el arreglo. 
nombre_escogido  = nombres[aleatorio] #Buscamos en el arreglo el nombre que concorde a la posicion de la variable "aleatorio".

print "El escogido es:",nombre_escogido #Mostramos por pantalla el nombre.
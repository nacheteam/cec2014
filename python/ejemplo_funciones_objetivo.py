import funciones_objetivo
import numpy as np

#Coges todas las funciones como una lista
funciones = funciones_objetivo.getFunciones()

#El tamaño del array puede ser el que quieras
print(funciones[0](np.zeros(10)))
print(funciones[5](np.zeros(30)))

#Devuelve el número de funciones
print(funciones_objetivo.getNumFunciones())

#Devuelve el límite inferior
print(funciones_objetivo.getLimInf())

#Devuelve el límite superior
print(funciones_objetivo.getLimSup())

#Devuelve el valor que da la funciones 2 y 7 en el óptimo
print(funciones_objetivo.getFuncMinValor(2))
print(funciones_objetivo.getFuncMinValor(7))

#Devuelve un diccionario con el límite superior e inferior del dominio y con el valor que da la función 5 en el óptimo.
print(funciones_objetivo.getInfo(5))

#Coge la función 3 y evalúa en [0,...,0]
f3 = funciones_objetivo.getFuncion(3)
print(f3(np.zeros(10)))

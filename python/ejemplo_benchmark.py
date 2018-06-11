import benchmark
import numpy as np

#Instancio la clase benchmark
bench = benchmark.Benchmark()

#Coges todas las funciones como una lista
funciones = bench.getFunciones()

#El tamaño del array puede ser el que quieras
print(funciones[0](np.zeros(10)))
print(funciones[5](np.zeros(30)))

#Devuelve el número de funciones
print(bench.getNumFunciones())

#Devuelve el límite inferior
print(bench.getLimInf())

#Devuelve el límite superior
print(bench.getLimSup())

#Devuelve el valor que da la funciones 2 y 7 en el óptimo
print(bench.getFuncMinValor(2))
print(bench.getFuncMinValor(7))

#Devuelve un diccionario con el límite superior e inferior del dominio y con el valor que da la función 5 en el óptimo.
print(bench.getInfo(5))

#Coge la función 3 y evalúa en [0,...,0]
f3 = bench.getFuncion(3)
print(f3(np.zeros(10)))

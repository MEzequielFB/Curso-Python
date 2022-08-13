import math #Importa el módulo math -> math ahora es un objeto, por lo tanto se pueden acceder a sus métodos
#https://docs.python.org/3/library/math.html -> Métodos de math

x = 2.9
print(math.ceil(x)) #Redondea para arriba
print(math.floor(x)) #Redondea para abajo

print(math.nextafter(x, 5))

print(round(x)) #Devuelve número redondeado
print(abs(-x)) #Devuelve valor absouluto
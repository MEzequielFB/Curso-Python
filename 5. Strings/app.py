course  = "Python's course for beginners"
print("1. "+ course) #Muestra por consola el string completo
print("2. "+ course[0]) #Muestra por consola el primer caracter del string
print("3. "+ course[-2]) #Muestra por consola el anteúltimo caracter del string

print("4. "+ course[0:3]) #Muestra por consola del primer caracter al tercero (excluye el cuarto caracter -> 3)
print("5. "+ course[0:]) #Muestra por consola del primer caracter al último (todo el string)
print("6. "+ course[1:3]) #Muestra por consola del segundo caracter al tercero (excluye al cuarto -> 3)

print("7. "+ course[1:-1]) #Muestra por consola del segundo caracter al anteúltimo (excluye al último caracter -> -1)

#String de varias líneas
course2 = """
Hi John,
Here is our first email

Thank you,
The support team
"""
print(course2) #Muestra por consola el string
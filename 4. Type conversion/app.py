birth_year = input("Birth year: ") #Pide por consola el anio de nacimiento
print(type(birth_year)) #Muestra por consola el tipo de la variable birth_year(string)

age = 2022 - int(birth_year) #birth_year da error si no lo convierto a int - Calcula la edad
print(type(age)) #Muestra el tipo de la variable age(int)
print(age) #Muestra age por consola
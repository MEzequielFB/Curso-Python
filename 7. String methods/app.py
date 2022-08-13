course = "Python for beginners"
#len devuelve el número de caracteres del string
print(len(course)) #Las funciones como print y len son funciones generales

#upper() no modifica el string, sino que crea uno nuevo y lo retorna
print(course.upper()) #Las funciones que son específicas para determinados objetos con llamadas métodos -> upper()
print(course.lower()) #Devuelve todo en minúscula
print(course.title()) #Devuelve string capitalizado
print(course)

#Devuelve el índice de la primera ocurrencia en el string
#Si devuelve -1 no encontró ninguna ocurrencia
#Caracteres en mayúscula y minúscula los toma distinto
print(course.find("p")) #Devuelve -1
print(course.lower().find("p")) #Devuelve el índice 0
print(course.find("beginners")) #Devuelve el índice 11 porque el caracter de la palabra está en esa posición

print(course.replace("beginners", "absolute beginners")) #Devuelve la variable con el texto indicado reemplazado. Mayúsculas y minúsculas los toma distinto
#Busca lo indicado en el string y devuelve un boolean
print("Python" in course) #Devuelve True
print("python" in course) #Devuelve False
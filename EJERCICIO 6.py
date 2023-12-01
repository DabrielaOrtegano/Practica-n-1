print("...................Ejercicio 2....................")
# Solicitar al usuario una cadena de caracteres en mayuscula
cadena_enmayuscula = input("Ingrese una cadena de caracteres en mayúscula: ")

# Dividir la cadena en palabras y convertirlas a minusculas
palabras_enminusculas = [palabra.lower() for palabra in cadena_enmayuscula.split()]

# Imprimir la lista con palabras en minuscula
print("Lista de palabras en minúscula:", palabras_enminusculas)
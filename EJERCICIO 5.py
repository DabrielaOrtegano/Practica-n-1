print("solicitar al usuario ingresar 3 numeros enteros: ")
input_1 = input("ingrese el primer numero entero: ")
input_2 = input("ingrese el segundo numero entero: ")
input_3 = input("ingrese el tercer numero entero: ")

# convertir a numeros enteros usando la funcion int
num_1 = int(input_1)
num_2 = int(input_2)
num_3 = int(input_3)

# crea una lista con los numeros ordenados 
lista_ordenada = [num_1, num_2, num_3]
print("Lista ordenada:", lista_ordenada)

# Ordenar lista de numeros

lista_ordenada.sort ()

print("lista con los numeros ordenados:", lista_ordenada)



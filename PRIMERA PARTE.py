print(".................Datos tipos numericos.................")
print("int")

# Enteros Int
entero_1 = 20
numero_1 = type(entero_1)
print("numero_1:", numero_1)


print(".................float..................")

# Flotantes
float_1 , float_2, float_3 = 0.348 , 10.5 ,1.5e2
tipo_float_1 = type(float_1)
print("float_1:", float_1)
print("float_2:", float_2)
print("float_3:", float_3)
print("type_float_1:", tipo_float_1)

print("..................complex......................")

# Numeros Complejos
complejo_1 = 2.1 + 7.8j
print("complejo_1:",complejo_1)
type_complejo_1=type(complejo_1)
print("type_complejo_1:",type_complejo_1)
print("type_complejo_1.img",complejo_1.imag)
print("type_complejo_1.real",complejo_1.real)
abs_complejo_1 = abs(complejo_1)
print("abs_complejo_1:", abs_complejo_1)

print("....................Datos tipo booleano.....................")
bool_1 = False
print("bool_1:", bool_1)
bool_2 = False
print("bool_2:",bool_2)
print("bool_1 == bool_2: ", bool_1 == bool_2)
bool_3 = 0
print("bool_3: ", bool_3)
bool_2 = False 
print("bool_2: ", bool_2)
print("bool_3 == bool_2: ", bool_3 == bool_2)
bool_4 = ""
print("bool_4: ", bool_4)
bool_2 = False
print("bool_2: ", bool_2)
print("bool_4 == bool_2: ", bool_4 == bool_2)
bool_5 = None
print("bool_5: ", bool_5)
bool_2 = False
print("bool_2: ", bool_2)
print("bool_5 == bool_2: ", bool_5 == bool_2)
bool_6 = []
print("bool_6: ", bool_6)
bool_2 = False
print("bool_2: ", bool_2)
print("bool_6 == bool_2: ", bool_6 == bool_2)
bool_7 = ()
print("bool_7: ", bool_7)
bool_2 = False
print("bool_2: ", bool_2)
print("bool_7 == bool_2: ", bool_7 == bool_2)
bool_8 = {}
print("bool_8: ", bool_8)
bool_2 = False
print("bool_2: ", bool_2)
print("bool_8 == bool_2: ", bool_8 == bool_2)
bool_9 = ['' , '']
print("bool_9: ", bool_9)
bool_2 = False
print("bool_2: ", bool_2)
print("bool_9 == bool_2: ", bool_9 == bool_2)

print("..........................................")
int_1 = int(bool_2)
print("int_1: ", int_1)

print("...........................................")
bool_10 = True
print("bool_10: ", bool_10)
int_2 = int(bool_10)
print("int_2: ", int_2)

print("...........................................")
tipo_bool10 = type(bool_10)
print("tipo_bool10: ", tipo_bool10)

str_bool10 = str(bool_10)
print("str_bool10: ", str_bool10)

tipo_str_1 = type(str(bool_10))
print("tipo_str_1: ", tipo_str_1)

tipo_bool1 = type(bool_1)
print("tipo_bool1: ", tipo_bool1)

str_2 = str(bool_2)
print("str_2: ", str_2)
tipo_str2 = type(str(bool_2))
print("tip2o_str2: ", tipo_str2)

print("............. Datos tipo arreglo..............")
print(".................list........................")

factura = ['pan' , 'huevos' , 100 , 1234]
print("factura: ", factura)

print("...................................................")
print("factura[0]: " , factura[0]) 
print("factura[3]: " , factura[3])

print(".....................................................")
numero_elementos = len(factura)
print("numero_elementos: ", numero_elementos)
numeros_elementosmenos1 = len(factura)-1
print("numeros_elementosmenos1: ", numeros_elementosmenos1)
print("factura[-1]: " , factura[-1])
print("factura[-len(factura)]: " , factura[-len(factura)])
factura = ['pan' , 'carne' , 'huevos' , 100 , 1234]
print("factura[1]: " , factura[1])
print("factura: " , factura)

print("................................................")
versiones_plone =[2.5 , 3.6 , 4 , 5] 
print("versiones_plone: " , versiones_plone)
versiones_plone.append(6)
print("versiones_plone: " , versiones_plone)

print(".................................................")
versiones_plone = [2.1 , 2.5 , 3.6 , 4 , 5 , 5 , 6]
print("versiones_plone.count(6): " , versiones_plone.count(6))
print("versiones_plone.count(5): " , versiones_plone.count(5))

print("............................................")
versiones_plone = [2.1 , 2.5 , 3.6]
print("versiones_plone: " , versiones_plone)
versiones_plone.extend([4])
print("versiones_plone: " ,versiones_plone)

print("..............................................")
versiones_plone = [2.1 , 2.5 , 3.6 , 4 , 5 , 6 , 4]
print("versiones_plone: " , versiones_plone)
print("versiones_plone.index(4): " , versiones_plone.index(4))

print(".............................................")
versiones_plone = [2.1 , 2.5 , 3.6 , 4 , 5 , 6]
print("versiones_plone: " , versiones_plone)
versiones_plone.insert( 2 , 3.7)
print("versiones_plone: " , versiones_plone)

print(".............................................")
versiones_plone = [4 , 2.5 , 5 , 3.6 , 2.1 , 6]
print("versiones_plone: " , versiones_plone)
versiones_plone.sort()
print("versiones_plone: " , versiones_plone)

print("................Datos tipo string...............")
print("................str.............................")
print("'Hola Mundo'")
hla_mnd = "'Hola Mundo'"
print("hla_mnd: " , hla_mnd)

print(".................................................")
a , b = "uno" , "dos"
print("a + b: ",  a + b)

print("..................................................")
c = "tres"
print("c * 3: " , c * 3)

print("...................................................")
tipo_calculo = "raiz cuadrada de dos"
valor = 2 ** 0.5
print("el resultado de {} es {}".format(tipo_calculo , valor))





















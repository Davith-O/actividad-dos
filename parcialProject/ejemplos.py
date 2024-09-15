#coneversion de tipos de datos
numero_entero = 10
numero_decimal = 3.14
cadena = "hola care bola"

print (type(numero_entero))
print(type(numero_decimal))
print(type(cadena))

#multilinea de cadenas
cadena_larga = """esta es una 
cadena que ocupa
varias lineas"""
print(cadena_larga)

#funcion len()
longitud = len(cadena)
print(longitud)

#subcadenas
subcadena_inicio = cadena[:5]
subcadena_medio = cadena[7:12]
subcadena_final = cadena[-5:]
print(subcadena_inicio, subcadena_medio, subcadena_final)

# Funciones upper() y lower()
cadena_mayuscula = cadena.upper()
cadena_minuscula = cadena.lower()
print(cadena_mayuscula, cadena_minuscula)

# Funcion strip()
cadena_con_espacios = "   Hola   "
cadena_sin_espacios = cadena_con_espacios.strip()
print(cadena_sin_espacios)

# Funcion replace()
cadena_nueva = cadena.replace("Hola", "Adios")
print(cadena_nueva)

# Funcion split()
palabras = cadena.split()
print(palabras)

# Formato de cadenas F-String
nombre = "Juan"
edad = 30
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(mensaje)
# Función para saludar
def saludar_alumno(nombre):
    print(f"Hola, {nombre}. Bienvenido a la práctica de Python.")

# Pedir nombre al usuario
nombre = input("Introduce tu nombre: ").strip()

# Comprobar si el nombre está vacío
if nombre == "":
    print("Error: debes introducir un nombre válido.")
else:
    saludar_alumno(nombre)
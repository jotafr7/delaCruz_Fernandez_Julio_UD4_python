# Lista donde se guardarán los ordenadores
ordenadores = []

# Bucle para introducir los datos de los ordenadores
while True:
    marca = input("Introduce la marca del ordenador (o escribe 'fin' para terminar): ")

    # Salir del programa
    if marca == "fin":
        break

    modelo = input("Introduce el modelo: ")
    ram = input("Introduce la memoria RAM: ")
    disco = input("Introduce la capacidad del disco: ")
    sistema = input("Introduce el sistema operativo: ")

    # Crear diccionario del ordenador
    ordenador = {
        "marca": marca,
        "modelo": modelo,
        "ram": ram,
        "disco": disco,
        "sistema_operativo": sistema
    }

    # Guardar el diccionario en la lista
    ordenadores.append(ordenador)

print("\n--- ORDENADORES REGISTRADOS ---")

# Mostrar todos los ordenadores
for posicion, ordenador in enumerate(ordenadores, start=1):
    print(f"\nOrdenador {posicion}")
    print(f"Marca: {ordenador['marca']}")
    print(f"Modelo: {ordenador['modelo']}")
    print(f"RAM: {ordenador['ram']}")
    print(f"Disco: {ordenador['disco']}")
    print(f"Sistema Operativo: {ordenador['sistema_operativo']}")
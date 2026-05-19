programas = ["Word", "Excel", "Acces", "PowerPoint"]

#Con este bucle se muestra la lista de programas con su posicion en la lista.
for posicion, programa in enumerate(programas, start=1):
    print(f"{posicion}. {programa}")
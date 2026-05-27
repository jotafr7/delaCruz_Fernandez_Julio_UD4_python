lista_programas = ["Word", "Excel", "Acces", "PowerPoint"]

#Con este bucle se muestra la lista de programas con su posicion en la lista.
for posicion, programa in enumerate(lista_programas):
    print(f"{posicion+1}. {programa}")
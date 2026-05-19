lista_perifericos = []

#Con este bucle se pide al usuario que introduzca el nombre de los perifericos que hay que comprar, y se guardan en una lista. El programa termina cuando se han introducido 5 perifericos.
for contador in range (5):
    nombre_perifericos = input("Introduce el nombre de los perifericos:")
    lista_perifericos.append(nombre_perifericos)

#Mostramos la lista de perifericos al usuario.
print("Los perifericos que hay que comprar son:")
print(lista_perifericos)
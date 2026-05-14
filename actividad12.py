#Preguntamos al usuario cuantos GB de memoria RAM tiene en su ordenador y se lo mostramos convertido a MB.
almacenamiento = int(input("Cuantas GB de memoria RAM tienes: "))

#Convertimos los GB a MB multiplicando por 1024, ya que 1 GB es igual a 1024 MB.
MB = almacenamiento * 1024

#Mostramos el resultado al usuario.
print(f"Tus GB en MB son: {MB} MB.")
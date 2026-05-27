contador = 0 
incidencias = input("Introducir incidencias:")

#Con este bucle se pide al usuario que introduzca las incidencias que se han registrado en el dia de hoy, y se cuenta el numero de incidencias. El programa termina cuando el usuario introduce "fin".
while incidencias != "fin":
    contador = contador + 1
    incidencias = input("Introduzca otra incidencia si lo requiere; si no escriba (fin) para salir.")

#Mostramos el numero de incidencias al usuario.
print(f"En el dia de hoy se han registrado {contador} incidencias.")
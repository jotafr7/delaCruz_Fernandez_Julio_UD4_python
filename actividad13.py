#Crea una lista
diccionario_componentes = []
fin_programa = ""

#Con este bucle se pide al usuario que introduzca los Watios de la ram, cpu y gpu, y se guardan en un diccionario. El programa termina cuando el usuario introduce "fin".
while fin_programa != "fin":
    ram = float(input("Introduce los Watios de la ram: "))
    cpu = float(input("Introduce los Watios de la cpu: "))
    gpu = float(input("Introduce los Watios de la gpu: "))
    componentes = {
        "ram": ram,
        "cpu": cpu,
        "gpu": gpu
    }
    fin_programa = input("Introduce fin, para terminar de meter componentes: ").lower()
    diccionario_componentes.append(componentes)

for componente in diccionario_componentes:
    print(f"Los Watios de la ram son: {componente['ram']} W")
    print(f"Los Watios de la cpu son: {componente['cpu']} W")
    print(f"Los Watios de la gpu son: {componente['gpu']} W")
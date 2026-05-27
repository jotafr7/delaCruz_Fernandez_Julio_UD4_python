# Función para calcular el precio con IVA
def calcular_iva(precio):
    precio_final = precio * 1.21
    
    return precio_final

# Pedir precio al usuario
precio = float(input("Introduce el precio del producto: "))

# Llamar a la función
resultado = calcular_iva(precio)

# Mostrar resultado
print(f"El precio con IVA es: {resultado} €")
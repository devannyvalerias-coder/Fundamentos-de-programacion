print("\nEjercicio 7 - Loop infinito")

# Queremos contar del 1 al 5
contador = 1

while contador <= 5:
    print(f"Número: {contador}")
    contador += 1  # 🔹 Faltaba esto: sin esto el while se vuelve infinito

print("Aquí terminan los ejercicios de while")

numeros = [10, 20, 30, 40, 50]
suma = 0
for num in numeros:
    suma += num
print(f"La suma total es: {suma}")

texto = "Alo, que haciendo mi gente en miércoles"
contador = 0
for letra in texto:
    if letra.lower() in "aeiou":
        contador += 1
print(f"Hay {contador} vocales")  # 🔹 "F" en minúscula y espacio entre Hay y {contador}

print("\nEjercicio 4")

numeros = [15, 42, 8, 23, 76, 31]
mayor = numeros[0]  # Empezamos con el primero de la lista
for num in numeros:
    if num > mayor:
        mayor = num  # 🔹 Faltaba actualizar la variable mayor

print(f"El número mayor es: {mayor}")  # 🔹 F minúscula

print("\nEjercicio 5")

cuadros = []
for i in range(1, 6):"  # Cambié el punto por coma (1. 6)"
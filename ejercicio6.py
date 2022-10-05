# Escribir un programa que lea un entero positivo,
# introducido por el usuario y después muestre
# en pantalla la suma de todos los enteros desde 1 hasta n.
# La suma de los  primeros enteros positivos puede
# ser calculada de la siguiente forma: (n * (n + 1)) / 2
numero = int(input("Introduce un número entero positivo: "))
while numero < 0:
    numero = int(input("Introduce un número entero positivo: "))
operacion = (numero * (numero + 1)) / 2
print("La suma de los números enteros de 1 a", numero, "es", int(operacion))
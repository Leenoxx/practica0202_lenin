# Escribir un programa que pregunte al usuario una
# cantidad a invertir, el interés anual y el número
# de años, y muestre por pantalla el capital obtenido en la inversión.
inversion = int(input("Ingresa la cantidad a invertir: "))
porcentaje = int(input("Ingresa el porcentaje de interés anual: "))
años = int(input("Ingresa la cantidad de años: "))
calculo = porcentaje * (1 / 100)
capital = inversion + (inversion * calculo * años)
print("El capital obtenido en la inversión es de", capital, "euros")
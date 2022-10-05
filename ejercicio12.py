# Una panadería vende barras de pan a 3.49€ cada una.
# El pan que no es del día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número
# de barras vendidas que no son del día. Después el
# programa debe mostrar el precio habitual de una barra
# de pan, el descuento que se le hace por no ser fresca
# y el coste final total.
barras_pan = int(input("Indica el número de barras vendidas "
                       "que no son del día: "))
precio_habitual = barras_pan * 3.49
descuento = precio_habitual * 0.6
coste_final = precio_habitual - descuento
print("El coste habitual es de", round(precio_habitual, 2), "€\n"
      "El descuento que se hace es de", descuento, "€\n"
      "El total a pagar es de", round(coste_final, 2), "€")
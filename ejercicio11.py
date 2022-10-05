# Imagina que acabas de abrir una nueva cuenta de ahorros
# que te ofrece el 4% de interés al año. Estos ahorros
# debido a intereses, que no se cobran hasta finales de año,
# se te añaden al balance final de tu cuenta de ahorros.
# Escribir un programa que comience leyendo la cantidad
# de dinero depositada en la cuenta de ahorros,
# introducida por el usuario. Después el programa
# debe calcular y mostrar por pantalla la cantidad
# de ahorros tras el primer, segundo y tercer años.
# Redondear cada cantidad a dos decimales.
dinero = float(input("Indica la cantidad de dinero depositada: "))
calculo_uno = dinero * 0.04
primer_año = dinero + calculo_uno
calculo_dos = primer_año * 0.04
segundo_año = primer_año + calculo_dos
calculo_tres = segundo_año * 0.04
tercer_año = segundo_año + calculo_tres
print("Total ahorros: \n -Primer año:", round(primer_año, 2), "€\n",
      "-Segundo año:", round(segundo_año, 2), "€\n", "-Tercer año:",
      round(tercer_año, 2), "€")
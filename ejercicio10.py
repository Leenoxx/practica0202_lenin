# Una juguetería tiene mucho éxito en dos de sus productos:
# payasos y muñecas. Suele hacer venta por correo y la
# empresa de logística les cobra por peso de cada paquete
# así que deben calcular el peso de los payasos y muñecas
# que saldrán en cada paquete a demanda. Cada payaso
# pesa 112 g y cada muñeca 75 g. Escribir un programa
# que lea el número de payasos y muñecas vendidos en el
# último pedido y calcule el peso total del paquete que será enviado.
payasos = int(input("Ingresa el número de payasos del pedido: "))
muñecas = int(input("Ingresa el número de muñecas del pedido: "))
calculo_uno = payasos * 112
calculo_dos = muñecas * 75
total = calculo_uno + calculo_dos
print("El peso total del paquete es de", total, "g")
# Escribir un programa que pregunte al usuario por el
# número de horas trabajadas y el coste por hora.
# Después debe mostrar por pantalla la paga que le corresponde.
horas = int(input("¿Cuántas horas has trabajado?"))
coste = int(input("¿Cuanto cobras la hora?"))
paga = horas * coste
print("La paga que te corresponde es de", paga, "euros.")

import csv

print("Abriendo archivo...")

with open("maestro_articulos.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    print("Leyendo filas...")
    for row in reader:
        print(row["codigo"], row["nombre_producto"])

print("Fin del script.")
import csv

print("Abriendo archivo...")

with open("maestro_articulos.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    print("Leyendo filas...")
    for row in reader:
        print(
            f"Código: {row['codigo']}, "
            f"Nombre: {row['nombre_producto']}, "
            f"Unidad: {row['unidad']}, "
            f"Proveedor: {row['proveedor']}"
        )

print("Fin del script.")
import pandas as pd


# Defino el diccionario de listas con los datos de ventas
datos = {
    "fecha": [
        "2026-01-03", "2026-01-05", "2026-01-08", "2026-01-12", "2026-01-15",
        "2026-01-20", "2026-01-25", "2026-02-02", "2026-02-06", "2026-02-10",
        "2026-02-14", "2026-02-18", "2026-02-22", "2026-03-01", "2026-03-05",
        "2026-03-09", "2026-03-14", "2026-03-18", "2026-03-23", "2026-03-28"
    ],
    "producto": [
        "Laptop", "Mouse", "Monitor", "Teclado", "Silla ergonómica",
        "Auriculares", "Escritorio", "Tablet", "Webcam", "Impresora",
        "Lámpara de escritorio", "Laptop", "Mouse", "Disco SSD", "Pendrive",
        "Monitor", "Estantería", "Disco externo", "Teclado", "Tablet"
    ],
    "categoria": [
        "Electrónica", "Accesorios", "Electrónica", "Accesorios", "Mobiliario",
        "Accesorios", "Mobiliario", "Electrónica", "Accesorios", "Electrónica",
        "Mobiliario", "Electrónica", "Accesorios", "Almacenamiento", "Almacenamiento",
        "Electrónica", "Mobiliario", "Almacenamiento", "Accesorios", "Electrónica"
    ],
    "unidades": [2, 15, 3, 8, 4, 10, 2, 5, 7, 1, 6, 3, 20, 9, 25, 2, 3, 4, 6, 2],
    "precio_unitario": [
        850.00, 12.50, 220.00, 35.00, 180.00,
        45.00, 310.00, 399.00, 60.00, 250.00,
        28.00, 850.00, 12.50, 95.00, 9.90,
        220.00, 120.00, 75.00, 35.00, 399.00
    ]
}

ventas = pd.DataFrame(datos) # Convierto el diccionario en tabla
ventas.to_csv("tarea_clase1/datos/ventas.csv", index=False) # Guardo la tabla en un archivo CSV llamado "ventas.csv" sin incluir el índice.
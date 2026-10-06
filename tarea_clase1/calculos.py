# Creo todas las fórmulas en la hoja de Cálculos para luego importarlas a Main.py

# Devuelve el total de venta por producto multiplicando las columnas "unidades" y "precio_unitario"
def total_venta(datos):
    return datos["unidades"] * datos["precio_unitario"]

# Devuelve el importe total de todas las ventas sumando la columna "total_venta"
def importe_total(datos):
    return datos["total_venta"].sum()

# Devuelve el total de unidades vendidas sumando la columna "unidades"
def unidades_vendidas(datos):
    return datos["unidades"].sum()

# Devuelve el total de ventas por categoría agrupando los datos por la columna "categoria" y sumando la columna "total_venta" para cada categoría
def total_por_categoria(datos):
    return datos.groupby("categoria")["total_venta"].sum()

# Devuelve el total de ventas para una categoría específica ingresada por el usuario
def obtener_ventas_por_categoria(datos):
    menu = {
        "1": "Electrónica",
        "2": "Accesorios",
        "3": "Mobiliario",
        "4": "Almacenamiento"
    }
    eleccion = input("Ingrese la categoría para obtener el total de ventas: 1. Electrónica, 2. Accesorios, 3. Mobiliario, 4. Almacenamiento: ")
    categoria = menu.get(eleccion) # aca usé un poco de IA para ver que atributo podia usar paras obtener el valor de la clave y comparar. Esto lo vimos en la clase de python aplicado a data science

    if categoria is None:
        print("Opción inválida. Por favor, elija una categoría válida.")
        return 0

    total = datos[datos["categoria"] == categoria]["total_venta"].sum()
    print(f"Total de ventas para la categoría '{categoria}' es: {total}")
    return total 

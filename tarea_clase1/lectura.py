import pandas as pd

# Aca use Gemini para crear la función. Tenia el contenido pero si quiero importarla en main tiene que ser función, para poder llamarla
def leer_ventas(ruta):
    try:
        ventas = pd.read_csv(ruta)
        return ventas
    except FileNotFoundError:
        print("No se ha encontrado el archivo de ventas")
        return None

# Aca cree una función tambien, usando la info del ejemplo de clase
def guardar_parquet(ventas, ruta):
    ventas.to_parquet(ruta, index=False)

# Aca cree una función tambien, usando la info del ejemplo de clase. Para poder mostrar si se guardó bien, lo guardo en una variable que me muestre el resultado
def leer_parquet(ruta):
    ventas_recuperadas = pd.read_parquet(ruta)
    return ventas_recuperadas


from lectura import leer_ventas # importo la función leer_ventas() de lectura.py
from calculos import total_venta, importe_total, unidades_vendidas, total_por_categoria, obtener_ventas_por_categoria # importo funciones de calculos.py
from lectura import guardar_parquet, leer_parquet # importo funciones de lectura.py para guardar y leer parquet

ventas = (leer_ventas("tarea_clase1/datos/ventas.csv"))# Print para comprobar que la tabla quedó bien 
if ventas is None:
    exit()
print(ventas)

ventas["total_venta"] = total_venta(ventas) # Llamo a la función total_venta() y guardo el resultado en una nueva columna llamada "total_venta".
print(ventas) # Compruebo que funcionó con un print
print(f"El importe total es: {importe_total(ventas)} €") # Print para mostrar le importe total llamando a la función
print(f"Las unidades vendidas son: {unidades_vendidas(ventas)} unidades") # Print para mostrar las unidades totales llamando a la función
print("\nTotal por categoría:\n", total_por_categoria(ventas)) # print para mostrar las ventas por categoria llamando a la función

obtener_ventas_por_categoria(ventas) # Llamo a la función obtener_ventas_por_categoria() para que el usuario pueda elegir una categoría y mostrar el total de ventas de esa categoría.

guardar_parquet(ventas,"tarea_clase1/datos/ventas.parquet") 
print(leer_parquet("tarea_clase1/datos/ventas.parquet"))

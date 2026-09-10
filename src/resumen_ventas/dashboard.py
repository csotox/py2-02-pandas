import pandas as pd

from cargar_datos import *

def main():
    print( get_ruta() )

    try:
        ordenes_entregadas = get_ordenes_entregadas()
        detalles_ordenes = get_detalles_ordenes()
    except FileNotFoundError as err:
        print( err )


    # DataFrame de ventas
    # Solo considera las ordenes entregadas
    ventas = detalles_ordenes.merge(
        ordenes_entregadas[['order_id']],
        on="order_id",
        how="inner"
    )

    # KPI
    ventas_totales = ventas["item_total"].sum()
    cantidad_pedidos = ordenes_entregadas['order_id'].nunique()
    ticket_promedio = ventas_totales / cantidad_pedidos

    print( f"Ventas totales: {ventas_totales:,}" )
    print( f"Cantidad de pedidos: {cantidad_pedidos:,}" )
    print( f"Ticket promedio: {ticket_promedio:,}" )




if __name__ == "__main__":
    main()

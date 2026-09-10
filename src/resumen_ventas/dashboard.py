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
    cantidad_clientes = ordenes_entregadas['customer_id'].nunique()

    # Tablero 1
    print( "\n" + "=" * 40 )
    print( f"{'Resumen de ventas':^40}" )
    print( "=" * 40 )


    print( f"{'Ventas totales:':<25} {ventas_totales:>13,.2f}" )

    print( f"{'Cantidad de pedidos:':<25} {cantidad_pedidos:>13,.0f}" )
    print( f"{'Ticket promedio:':<25} {ticket_promedio:>13,.2f}" )
    print( f"{'Cantidad de clientes:':<25} {cantidad_clientes:>13,.0f}" )

    print( "=" * 40 )



if __name__ == "__main__":
    main()

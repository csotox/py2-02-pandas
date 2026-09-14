import pandas as pd
import matplotlib.pyplot as plt

from cargar_datos import *

def card(ax, titulo: str, valor: str, color: str = "blue") -> None:
    ax.text(
        0.5, 0.65,
        titulo,
        ha="center", va="center",
        fontsize=12
    )

    ax.text(
        0.5, 0.35,
        valor,
        ha="center", va="center",
        fontsize=14, fontweight='bold', color=color
    )

    ax.set_xticks([])
    ax.set_yticks([])


def generar_dashboard(kpi):
    fig, axes = plt.subplots(2, 4, figsize=(17, 4))

    card(axes[0, 0], "Ventas totales", f"{kpi['ventas_totales']:,.2f}")
    card(axes[0, 1], "Cantidad de pedidos", f"{kpi['cantidad_pedidos']:,.0f}", "green")
    card(axes[0, 2], "Ticket promedio", f"{kpi['ticket_promedio']:,.2f}")
    card(axes[0, 3], "Cantidad de clientes", f"{kpi['cantidad_clientes']:,.0f}", "red")


    plt.show()


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

    kpi = {
        "ventas_totales": ventas_totales,
        "cantidad_pedidos": cantidad_pedidos,
        "ticket_promedio": ticket_promedio,
        "cantidad_clientes": cantidad_clientes
    }

    generar_dashboard(kpi)



if __name__ == "__main__":
    main()

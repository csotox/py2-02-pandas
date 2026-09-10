import pandas as pd

from cargar_datos import *

def main():
    print( get_ruta() )

    try:
        ordenes_entregadas = get_ordenes_entregadas()
        detalles_ordenes = get_detalles_ordenes()
    except FileNotFoundError as err:
        print( err )

    print(
        ordenes_entregadas[
            [ 'order_id', 'customer_id', 'status' ]
        ].head()
    )


    # print( detalles_ordenes )

if __name__ == "__main__":
    main()

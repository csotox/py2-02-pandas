import pandas as pd

from cargar_datos import get_ruta, cargar_csv

def main():
    print( get_ruta() )

    try:
        algo = cargar_csv('products.csv')
    except FileNotFoundError as err:
        print( err )

    print( algo )

if __name__ == "__main__":
    main()

import pandas as pd

def inicio():
    print("Ejemplo de Serie de Pandas")

    lista_precios = [100, 500, 600, 150, 400]

    # print( type(lista_precios) )
    # print( lista_precios )

    precios = pd.Series(lista_precios)
    print( type(precios) )
    print( precios )

    print()
    print("Ejemplo de DataFrame de Pandas" )
    venta = {
        "producto": ["Producto 1", "Producto 2", "Producto 3"],
        "precio": [10, 25, 18]
    }
    print( type(venta) )
    print( venta )

    df_venta = pd.DataFrame(venta)
    print( type(df_venta) )
    print( df_venta )

def get_productos():
    df = pd.read_csv("data/products.csv", )

    return df

def main():
    # print("Hola mundo")
    # inicio()

    df_productos = get_productos()
    # print( df_productos )

    # Imprime/muestra las primeras 5 filas
    # print( df_productos.head() )
    # print( df_productos.head(10) )

    # Imprimir/mostrar las últimnas filas
    # print( df_productos.tail() )
    # print( df_productos.tail(15) )

    # Obtener filas aleatorias
    # print( df_productos.sample(5) )

    # Tamaño del DataFrame
    # Tupla -> (Filas, Columnas)
    # print( df_productos.shape )

    # Columnas
    # print( type( df_productos ) )
    # print( df_productos.columns )

    # Índices
    # print( df_productos.index )

    # Informasción general sobre el DataFrame
    # print( df_productos.info() )

    # Tipo de datos de la columna
    # print( df_productos.dtypes )

    # Estadistica descriptiva
    # print( df_productos.describe() )

    # Funciones de agregado
    # print( df_productos['stock'].sum() )



if __name__ == "__main__":
    main()

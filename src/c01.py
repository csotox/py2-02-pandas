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

def get_clientes():
    df = pd.read_csv("data/customers.csv", )

    return df

def main():
    # print("Hola mundo")
    # inicio()

    df_productos = get_productos()
    df_clientes = get_clientes()
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

    #-- - -----------------------------------------------
    #-- - Pandas selección, filtrado e índices
    #-- - -----------------------------------------------

    #-- - Obtener por nombre de la columna fijo
    #-- - --------------------------------------
    # print( 
    #     df_productos[
    #         'product_name'
    #     ]
    # )

    #-- - Obtener por nombre de la columna dinámico
    #-- - ------------------------------------------
    # col = 'product_name'
    # print( df_productos[col]  )

    #-- - Devolver varias columnas
    #-- - Debo enviar como argumento una lista list []
    #-- - ------------------------
    # print(
    #     df_productos[
    #         [
    #             'product_id',
    #             'product_name',
    #             'stock'
    #         ]
    #     ]
    # )

    #-- - Diferencia entre Serie y DataFrame al obtener columnas
    #-- - ------------------------------------------------------

    #-- - Obtenemos una serie
    # print( type( df_productos[ 'product_name' ] ) )

    #-- - Obtenemos un DataFrame
    # print( type( df_productos[ [ 'product_name' ] ] ) )


    #-- - Obtener valores usando los métodos iloc y loc
    #-- - ---------------------------------------------

    #-- - iloc[] selección por posición
    #-- - Cumple con las reglas Slice de Python

    #-- - Obtener filas
    # print( df_productos.iloc[5] )
    # print( df_productos.iloc[4:8] )

    """
    Recordar que Slice el valor final no es incluido
    (inicio, fin]
    i >= inicio and i < fin
    """

    #-- - Obtener filas y columnas
    #-- -                      Filas      Columnas
    # print( df_productos.iloc[4:8,       [0, 1, 5]] )

    #-- - Base de comparación
    # print( df_productos.iloc[0:3, [0, 1]] )

    #-- - loc selecciona por etiqueta
    # print( df_productos.loc[0:3] )

    # print( df_productos.loc[0:2, ['product_id', 'product_name']] )

    #-- - Filtros booleanos
    #-- - -----------------

    # condicion = df_productos["unit_price"] > 500

    # print( condicion )

    # print(
    #     f"Productos con precio mayores a 500: {condicion.sum()}"
    # )

    # prod_mayor_500 = df_productos[ condicion ]
    # print( prod_mayor_500 )

    #-- - Filtrar valores categóricos
    # prod_electronica = df_productos[
    #     df_productos["category"] == 'Electrónica'
    # ]

    # print( prod_electronica[
    #     [
    #         'product_id', 'product_name', 'category', 'stock']
    #     ]
    # )

    """
    Operadores lógicos
    - - - - - - - - - -
    -> Y = &
    -> O = |
    -> NOT = ~
    -> Debemos utilizar paréntesis para cada operación de comparación
    """

    # prod_electronica = df_productos.loc[
    #     (df_productos["category"] == 'Electrónica')
    #         & (df_productos["stock"] > 100),
    #     ['product_id', 'product_name', 'category', 'stock']
    # ]

    # print( prod_electronica[
    #     [
    #         'product_id', 'product_name', 'category', 'stock']
    #     ]
    # )

    #-- - Filtrar valores categóricos
    # condicion = df_productos['category'] == 'Mascotas'
 
    # print(df_productos.loc[condicion, ['product_id', 'product_name', 'category']])

    #-- - Operador `isin()`
    # print( df_productos.head() )

    #-- - De manera tradicional utilizamos un if y un Or para filtrar
    #-- - por varias categoría. Esto tiene varios problemas:
    #-- - La condición queda fija
    # r1 = df_productos[
    #     ( df_productos['category'] == 'Juguetes' ) |
    #     ( df_productos['category'] == 'Libros' )
    # ]

    # print( r1 )

    #-- - Utilizando isin() podemos pasar una lista/tupla generada de manera
    #-- - dinámica y esto hace más flexible la condición.
    # categorias = ( 'Juguetes', 'Libros' )

    # r2 = df_productos[
    #     ( df_productos['category'].isin(categorias) )
    # ]

    # print( r2 )

    #-- - Uso de `between()`
    #-- - Nos facilita aplicar filtro para a un rango
    # r3 = df_productos[
    #     ( df_productos['unit_price'] >= 500 ) &
    #     ( df_productos['unit_price'] <= 600 )
    # ]

    # print( r3 )

    #-- - Mismo resultado, más legible
    # r4 = df_productos[
    #     ( df_productos['unit_price'].between(500, 600 ) )
    # ]

    # print( r4 )

    #-- - -----------------------------------------------
    #-- - Ordenar DataFrame
    #-- - -----------------------------------------------
    # top_10_prod_precio = df_productos.sort_values(
    #     "unit_price",
    #     ascending=False
    # ).head(15)

    # print( top_10_prod_precio )

    # r5 = df_productos.loc[
    #     ( df_productos['category'] == 'Juguetes' ),
    #     ["product_id", "product_name", "category", "unit_price", "stock"]
    # ].sort_values(
    #     "unit_price",
    #     ascending=False
    # ).head(10)

    # print( r5 )

    #-- - -----------------------------------------------
    #-- - Índices
    #-- - -----------------------------------------------

    # print( r5.index )

    # # reset_index() regresa un nuevo DataFrame
    # print( r5.reset_index() )

    #-- - Si deseamos modificar el DF actual debemos usar el argumento `inplace`
    # print( r5.reset_index( inplace=True ) )
    # print( r5.index )
    # print( r5 )

    #-- - -----------------------------------------------
    #-- - Pandas calidad de los datos
    #-- - -----------------------------------------------

    #-- - Vista general de los datos
    # print( df_productos.shape )
    # print( df_productos.head() )
    # print( df_productos.info() )

    #-- - Gestión de Valores faltantes
    # df_prod_faltan = df_productos.isna().sum()

    # print( df_prod_faltan )
    # print( type(df_prod_faltan) )

    # 3 vías de acción para trabajar con faltantes
    #-- - ------------------------------------------
    # 1. Eliminar las filas con valores faltantes
    # 2. Rellenar / imputar
    # 3. Conservar original

    #-- - Mostrar solo columnas con valores faltantes
    # solo_faltantes = df_prod_faltan[ df_prod_faltan > 0 ]
    # print( solo_faltantes )

    #-- - Productos sin marca
    # prod_sin_marca = df_productos.loc[
    #     df_productos["brand"].isna(),
    #     ["product_id", "product_name", "brand"]
    # ]

    # print( prod_sin_marca )

    #-- - Productos con marca
    # prod_con_marca = df_productos.loc[
    #     df_productos["brand"].notna(),
    #     ["product_id", "product_name", "brand"]
    # ]

    # print( prod_con_marca )
    # print( id(prod_con_marca) )
    # prod_con_marca = None
    # print( id(prod_con_marca) )

    #-- - Eliminar variable de la memoria
    # del prod_con_marca
    # print( id(prod_con_marca) )

    #-- - productos completos (Sin celdas con valores faltantes)
    # df_prod_sin_faltante = df_productos.dropna()

    # print( df_prod_sin_faltante.shape )

    # 2. Reemplazar valores faltantes / imputación
    # prod_sin_marca2 = df_productos.loc[
    #     df_productos["brand"].isna() |
    #         df_productos["weight_g"].isna(),
    #     ["product_id", "product_name", "brand", "weight_g"]
    # ]

    # print( prod_sin_marca2 )

    # prod_sin_marca2["brand"] = prod_sin_marca2["brand"].fillna("Sin marca")

    # print( prod_sin_marca2 )


    # Valores inconsistentes
    #-- - ------------------
    # print( df_productos.columns )
    # categoria = df_productos["category"].unique()
    # print( categoria )

    # for item in categoria:
    #     print( f"[{item}]" )

    # Establecer la cantidad de valores unicos para la columna Category
    # cant_category = len( categoria )
    # print( f"Cantidad de categorías {cant_category}" )

    # if cant_category > 10:
    #     Envíar alerta asumiendo que no deben existir más de 10 categorías

    # Hacemos una copia para mantener el original
    # df_aux   = df_productos.copy()
    # df_aux_h = df_productos.copy()

    # Quitar espacios en blanco
    # df_aux["category"] = df_aux["category"].str.strip()

    # Normalizar a letra capital
    # df_aux["category"] = df_aux["category"].str.capitalize()

    # Usando métodos encadenados
    # df_aux["category"] = df_aux["category"].str.strip().str.capitalize()

    # categoria_nueva = sorted( df_aux["category"].unique() )
    # cant_category_real = len( categoria_nueva )
    # for item in categoria_nueva:
    #     print( f"[{item}]" )

    # print( f"cantidad de categorías real: {cant_category_real}")

    # Alternativa para normalizar textos
    # Técnica de Homologación (Diccionario)
    # Ejemplo de caso de uso
    #   santiago
    #   Santiago
    #   saniago
    #   santiago centro
    #   stgo

    # cate_real = {
    #     " deportes ": "Deportes",
    #     " juguetes ": "Juguetes",
    #     " belleza ": "Belleza",
    #     " ropa ": "Hogar",
    #     " accesorios ": "Accesorios",
    # }
    # df_aux_h["category"] = df_aux_h["category"].replace( cate_real )

    # categoria_nueva = sorted( df_aux_h["category"].unique() )
    # cant_category_real = len( categoria_nueva )
    # for item in categoria_nueva:
    #     print( f"[{item}]" )

    # print( f"cantidad de categorías real: {cant_category_real}")

    #-- - ------------------
    #-- - Valores duplicados
    #-- - ------------------

    # Exploración inicial
    # print( df_clientes.shape )
    # print( df_clientes )
    # print( df_clientes.columns )

    # Devuelve una serie booleana
    # 1. Considera toda la fila.
    # 2. Mantiene como original la primera fila
    # 3. Considera duplicada a partir de la siguiente aparición
    # duplicados = df_clientes.duplicated()
    # print( duplicados )

    # print( duplicados.sum() )

    # clientes_duplicados = df_clientes[ duplicados ]
    # print( clientes_duplicados )

    # print( "Muestra todas las filas duplicadas")
    # clientes_duplicados_todos = df_clientes[
    #     df_clientes.duplicated( keep=False )
    # ].sort_values("customer_id")
    # print( clientes_duplicados_todos )

    # NOTA: `duplicated()` toma todos los valores de la fila
    # Si tenemos una columna de `id` unica no tendremos
    # valores duplicados
    # Columna de identidad con las siguientes características:
    # Valor entero (int) + unico

    # Calcular los duplicados por columnas especificas/determinadas
    # print( "Muestra duplicados por columnas especificas")
    # duplicado_por_columna = df_clientes[
    #     df_clientes.duplicated( 
    #         subset=['customer_name', 'city']
    #     )
    # ].sort_values("customer_id")
    # print( duplicado_por_columna )

    #-- - Eliminar duplicados
    #-- - -------------------
    # print( f"Número de clientes del dataset: {len(df_clientes):,}")
    # df_clientes = df_clientes.drop_duplicates()
    # print( f"Número de clientes reales: {len(df_clientes):,}")

    #-- - ----------------
    #-- - Valores atípicos
    #-- - ----------------

    print( df_productos["unit_price"].describe() )

    # print(
    #     df_productos.sort_values("unit_price", ascending=False)
    # )

    # z-score
    # iqr

    #-- - Calcular el z-score
    media = df_productos["unit_price"].mean()
    desviacion = df_productos["unit_price"].std()

    df_productos["z-score"] = (
        (df_productos["unit_price"] - media) / desviacion
    )

    print(
        df_productos.loc[
            df_productos["z-score"].abs() > 3,
            ["product_name", "unit_price", "z-score"]
        ]

    )

    #-- - Calcular IQR
    q1 = df_productos["unit_price"].quantile(0.25)
    q3 = df_productos["unit_price"].quantile(0.75)

    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    print( f"Q1: {q1}" )
    print( f"Q3: {q3}" )
    print( f"IQR: {iqr}" )
    print( f"Limite inferior: {limite_inferior}" )
    print( f"Limite superior: {limite_superior}" )



if __name__ == "__main__":
    main()

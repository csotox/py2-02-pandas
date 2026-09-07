import numpy as np
import pandas as pd

def get_productos():
    df = pd.read_csv("data/products.csv", )

    return df

def get_clientes():
    df = pd.read_csv("data/customers.csv", )

    return df

def main():
    df_productos = get_productos()
    # df_clientes = get_clientes()
    # print( df_productos )

    #-- - ------------------------
    #-- - Operaciones vectorizadas
    #-- - ------------------------
    # print( df_productos[[
    #         "product_name",
    #         "unit_cost",
    #         "unit_price"
    #     ]]
    # )

    #-- - Calcular el Margen
    #-- - ------------------

    # Valor absoluto
    df_productos["margen"] = (
        df_productos["unit_price"] - df_productos["unit_cost"]
    )

    # Valor relativo
    df_productos["margen_pct"] = (
        (df_productos["unit_price"] / df_productos["unit_cost"]) * 100
    )

    # # Renombrar columna individualmente
    # df_productos = df_productos.rename(
    #     columns={
    #         "margen": "utilidad",
    #         "margen_pct": "utilidad_pct"
    #     }
    # )

    # print( df_productos[[
    #         "product_name",
    #         "unit_cost",
    #         "unit_price",
    #         "utilidad",
    #         "utilidad_pct"
    #     ]].head(10)
    # )

    #-- - --------------------------------------
    #-- - Crear columna de categoría condicional
    #-- - --------------------------------------

    # Marcar productos con stock inferior a 20 unidades
    # como Crítico
    # where() de Pandas
    # where() -> Si la condición es True, devuelve el valor original
    #         -> Si la condición es False, devuelve el valor alternativo
    # df_productos["stock_status"] = (
    #     df_productos["stock"].where(df_productos["stock"] >= 20, "Crítico")
    # )

    # where() de Numpy
    # Funciona como un if() tradicional
    df_productos["stock_status"] = np.where(
            df_productos["stock"] < 20,
            "Crítico",
            "Normal"
        )

    print( df_productos.loc[
        ( df_productos["stock"] < 30 ),
        [
            "product_name",
            "unit_cost",
            "unit_price",
            "stock",
            "stock_status"
        ]]
    )









if __name__ == "__main__":
    main()

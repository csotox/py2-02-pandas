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





if __name__ == "__main__":
    main()

import pandas as pd
import matplotlib.pyplot as plt

def get_productos():
    df = pd.read_csv("data/products.csv", )

    return df

def mi_primer_grafico():
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 18, 16, 25]

    # Creamos el lienzo de trabajo
    plt.figure()

    plt.plot(x, y)

    plt.show()

def main():
    df = get_productos()

    # print( df.describe() )
    mi_primer_grafico()

if __name__ == '__main__':
    main()

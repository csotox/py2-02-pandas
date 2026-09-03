import pandas as pd
import matplotlib.pyplot as plt

def get_productos():
    df = pd.read_csv("data/products.csv", )

    return df

def mi_primer_grafico():
    x = [1, 2, 3, 4, 5]
    y = [10, 12, 18, 16, 25]

    # Creamos el lienzo de trabajo
    # 10 = ancho
    #  5 = alto
    plt.figure( figsize=(10, 5) )

    plt.plot(x, y)

    # Agregar títulos
    plt.title("Esto es el título del gráfico")
    plt.xlabel("Label del Eje X")
    plt.ylabel("Label del Eje Y")

    # plt.grid(True, linestyle="--")
    plt.grid(axis="y", linestyle="--", color="green")
    plt.grid(axis="x", linestyle="--", color="yellow")

    plt.axhline(18, linestyle="--", color="red", label="Ref Y=18")
    plt.axvline( 3, linestyle="--", color="red", label="Ref X=3")

    # Anotar el punto (3, 18)
    plt.annotate(
        "Punto (3, 18)",          # Texto de la anotación
        xy=(3, 18),               # Coordenadas del punto
        xytext=(3.5, 20),         # Posición del texto
        arrowprops=dict(
            facecolor="black",    # Color de la flecha
            shrink=0.05,          # Ajuste de tamaño
            width=1,              # Grosor de la flecha
            headwidth=8           # Tamaño de la cabeza
        )
    )

    plt.legend()

    # plt.show()
    plt.savefig('output/mi_primer_grafico.png')
    plt.close()

def analisis_precios(data):

    # Crear figura con dos subplots horizontales
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # Histograma
    axes[0].hist(data["unit_price"], bins=30)
    axes[0].set_title("Distribución de unit_price")
    axes[0].set_xlabel("Precio")
    axes[0].set_ylabel("Frecuencia")

    # Boxplot
    axes[1].boxplot(data["unit_price"], orientation="horizontal")
    axes[1].set_title("Boxplot de unit_price")
    axes[1].set_xlabel("Precio")


    plt.tight_layout()
    # plt.show()
    plt.savefig('output/tablero.png')
    plt.close()


def main():
    df = get_productos()

    # print( df.describe() )
    # mi_primer_grafico()
    analisis_precios(df)

if __name__ == '__main__':
    main()

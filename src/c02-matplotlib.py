import pandas as pd
import matplotlib.pyplot as plt

def get_productos():
    df = pd.read_csv("data/products.csv", )

    return df

def main():
    df = get_productos()

    print( df.describe() )

if __name__ == '__main__':
    main()

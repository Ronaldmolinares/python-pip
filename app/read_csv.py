import pandas as pd


def read_csv(path):
    """
    Lee un archivo CSV y retorna un DataFrame de pandas.
    """
    df = pd.read_csv(path)
    return df


if __name__ == "__main__":
    result = read_csv("./app/data.csv")
    print(result.head())
    print("::" * 15)
    print(result.info())
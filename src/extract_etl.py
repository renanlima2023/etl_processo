import pandas as pd

def extract(path):
    """
    Extrai dados de um arquivo CSV.

    Args:
        path (str): Caminho para o arquivo CSV.

    Returns:
        pandas.DataFrame: DataFrame contendo os dados extraídos.
    """
    df = pd.read_csv(path)
    return df
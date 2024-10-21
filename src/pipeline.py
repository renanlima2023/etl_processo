from extract_etl import extract
from transform_etl import transform
from load_etl import load

def pipeline(path):
    """
    Executa o pipeline completo de ETL.

    Args:
        path (str): Caminho para o arquivo CSV de entrada.

    Etapas:
    1. Extrai dados do arquivo CSV
    2. Transforma e limpa os dados
    3. Carrega os dados processados em um arquivo Parquet    """
    df = extract(path)
    df = transform(df)
    load(df)
pipeline("data/input/vendas.csv")
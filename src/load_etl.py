def load(df):
    """
    Salva o DataFrame processado em formato Parquet.

    Args:
        df (pandas.DataFrame): DataFrame a ser salvo.

    Saída:
        Arquivo 'vendas.parquet' salvo no diretório 'data/output/'.
    """
    df.to_parquet("data/output/vendas.parquet")
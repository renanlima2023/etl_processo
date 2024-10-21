import pandas as pd
def transform(df):
    """
    Processa e limpa os dados do DataFrame.

    Args:
        df (pandas.DataFrame): DataFrame original a ser transformado.

    Returns:
        pandas.DataFrame: DataFrame transformado e limpo.

    Transformações realizadas:
    - Remove duplicatas
    - Trata valores nulos em 'quantidade' e 'valor_total'
    - Cria coluna 'mes' baseada na coluna 'data'
    - Cria coluna 'valor_total' se não existir
    """
    # Remover duplicatas
    df = df.drop_duplicates()
    
    # Tratar valores nulos
    df['quantidade'] = df['quantidade'].fillna(0)
    df['valor_total'] = df['valor_total'].fillna(df['quantidade'] * df['valor_unitario'])
    
    # Criar coluna 'mes'
    df['mes'] = pd.to_datetime(df['data']).dt.month
    
    # Criar coluna 'valor_total' (caso não exista)
    if 'valor_total' not in df.columns:
        df['valor_total'] = df['quantidade'] * df['valor_unitario']
    
    return df
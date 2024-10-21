# ETL Processo

Este projeto contém um processo ETL (Extract, Transform, Load) desenvolvido em Python.

## Requisitos

- Python 3.7+
- Git

## Instalação

Siga estas etapas para configurar o projeto em sua máquina local:

1. Clone o repositório:
   ```
   git clone git@github.com:renanlima2023/etl_processo.git
   ```

2. Navegue até o diretório do projeto:
   ```
   cd etl_processo
   ```

3. Crie um ambiente virtual:
   ```
   python -m venv .venv
   ```

4. Ative o ambiente virtual:
   - No Windows:
     ```
     .venv\Scripts\activate
     ```
   - No macOS e Linux:
     ```
     source .venv/bin/activate
     ```

5. Instale as dependências do projeto (assumindo que existe um arquivo requirements.txt):
   ```
   pip install -r requirements.txt
   ```
## Uso
Para rodar o projeto execute o comando abaixo:
python src/pipeline.py

## Estrututa do Projeto
`data/input/vendas.csv`: Aquivo contendo dados de vendas.
`data/ouput/vendas.parquet`: Arquivo Parquet contendo os dados transformados.
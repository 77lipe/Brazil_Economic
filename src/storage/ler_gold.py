import pandas as pd
from src.config.caminhos import CAMINHO_GOLD

COLUNAS_OBRIGATORIAS_GOLD = {
    "data",
    "valor",
    "indicador",
    "nome",
    "unidade"
}

def carregar_dados_gold(nome_tabela: str = "indicadores_bcb")-> pd.DataFrame:
    if not isinstance(nome_tabela, str):
        raise TypeError(
            f"Nome da tabela Gold não pode estar vazio."
        )
    if not nome_tabela.strip():
        raise ValueError(
            f"O nome da tabela não pode estar vazio."
        )

    caminho_arquivo = CAMINHO_GOLD / f"{nome_tabela}.parquet"
    if not caminho_arquivo.is_file():
        raise FileNotFoundError(
            f"Arquivo Gold não encontrado: {caminho_arquivo}"
        )

    dataframe = pd.read_parquet(caminho_arquivo)
    if dataframe.empty:
        raise ValueError(
            "O arquivo Gold não possui registros"
        )

    colunas_ausentes = (
        COLUNAS_OBRIGATORIAS_GOLD - set(dataframe.columns)
    )
    if colunas_ausentes:
        raise ValueError(
            f"Colunas obrigatórias ausentes\n{sorted(colunas_ausentes)}"
        )

    dataframe = dataframe.sort_values(
        by=["data", "indicador"]
    ).reset_index(drop=True)

    return dataframe
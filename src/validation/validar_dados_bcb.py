""" Validação das informações recebidas pela API """

import pandas as pd

COLUNAS_OBRIGATORIAS = {"data", "valor"}
def validar_dados_bcb(dataframe: pd.DataFrame) -> None:
    
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError(
            "O objeto recebido não é um DataFrame"
        )
    
    if dataframe.empty:
        raise ValueError(
            "DataFrame retornado pela API está vazio"
        )

    colunas_ausentes = (
        COLUNAS_OBRIGATORIAS - set(dataframe.columns)
    )
    if colunas_ausentes:
        raise ValueError(
            f"Colunas obrigatórias ausentes: \n{sorted(colunas_ausentes)}"
        )

    if dataframe["data"].isna().any():
        raise ValueError(
            "A coluna 'data' possui valores nulos"
        )

    if dataframe["valor"].isna().any():
        raise ValueError(
            "A coluna 'valor' possui valores nulos"
        )
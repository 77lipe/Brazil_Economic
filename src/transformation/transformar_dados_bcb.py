""" Transformações dos dados extraídos do BCB """

import pandas as pd 
from src.config.indicadores_bcb import INDICADORES_BCB

def transformar_dados_bcb(dataframe: pd.DataFrame, nome_indicador: str)-> pd.DataFrame:

    indicador = INDICADORES_BCB.get(nome_indicador)
    if indicador is None:
        raise ValueError(
            f"Indicador '{nome_indicador} não encontrado'"
        )

    df_transformado = dataframe.copy()

    df_transformado["data"] = pd.to_datetime(
        df_transformado["data"],
        format="%d/%m/%Y",
        errors="raise"
    )

    df_transformado["valor"] = pd.to_numeric(
        df_transformado["valor"],
        errors="raise"
    )

    df_transformado["indicador"] = nome_indicador

    for nome_coluna, valor_metadado in indicador.items():
        df_transformado[nome_coluna] = valor_metadado
            
    df_transformado["fonte"] = "Banco Central do Brasil"

    df_transformado["ano"] = (
        df_transformado["data"].dt.year
    )
    df_transformado["mes"] = (
        df_transformado["data"].dt.month
    )
    df_transformado["dia"] = (
        df_transformado["data"].dt.day
    )

    df_transformado = df_transformado.sort_values(
        by="data"
    ).reset_index(drop=True)

    return df_transformado
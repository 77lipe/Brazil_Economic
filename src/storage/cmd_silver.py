""" Função de Camada Silver - Armazenar os Dados tratados """

from datetime import datetime
from pathlib import Path

import pandas as pd

from src.config.caminhos import CAMINHO_SILVER
from src.config.converter_data import formatar_data


def salvar_silver(
        dataframe_tratado: pd.DataFrame,
        nome_indicar: str,
        data_inicial: str,
        data_final: str
) -> Path:

    if dataframe_tratado.empty:
        raise ValueError(
            f"DataFrame recebido está vazio, não foi possível salvar dados na SILVER"
        )

    CAMINHO_SILVER.mkdir(
        parents=True,
        exist_ok=True
    )

    data_inicial_formatada = formatar_data(data_inicial)
    data_final_formatada = formatar_data(data_final)
    nome_arquivo = (
        f"{nome_indicar}_"
        f"{data_inicial_formatada}_"
        f"{data_final_formatada}.parquet"
        )

    caminho_arquivo = CAMINHO_SILVER / nome_arquivo

    dataframe_tratado.to_parquet(
        caminho_arquivo,
        index=False,
        engine="pyarrow"
    )

    return caminho_arquivo
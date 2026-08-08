""" Função de Camada Silver - Armazenar os Dados tratados """

from datetime import datetime
from pathlib import Path

import pandas as pd

CMD_SILVER = Path("data/silver")

def salvar_silver(
        dataframe_tratado: pd.DataFrame,
        nome_indicar: str
) -> Path:

    CMD_SILVER.mkdir(
        parents=True,
        exist_ok=True
    )

    nome_arquivo = f"{nome_indicar}.parquet"

    caminho_arquivo = CMD_SILVER / nome_arquivo

    dataframe_tratado.to_parquet(
        caminho_arquivo,
        index=False,
        engine="pyarrow"
    )

    return caminho_arquivo
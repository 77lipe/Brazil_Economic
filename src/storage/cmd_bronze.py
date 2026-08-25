""" Camada Bronze - Armazenamento dos dados brutos """

from datetime import datetime
from pathlib import Path

import pandas as pd 

from src.config.caminhos import CAMINHO_BRONZE


def salvar_bronze(
    dataframe: pd.DataFrame,
    nome_indicador: str
) -> Path:

    CAMINHO_BRONZE.mkdir(
        parents=True,
        exist_ok=True
    )

    data_executacao = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = (
        f'{nome_indicador}_{data_executacao}.json'
    )

    caminho_arquivo = CAMINHO_BRONZE / nome_arquivo

    dataframe.to_json(
        caminho_arquivo, 
        orient='records',
        force_ascii=False,
        indent=4,
    )

    return caminho_arquivo
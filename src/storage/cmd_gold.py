""" Função para guardar o dataFrame final na CAMADA - GOLD"""

from pathlib import Path
import pandas as pd

CAMINHO_GOLD = Path("data/gold")
def salvar_gold(
        dataframe: pd.DataFrame,
        nome_tabela: str
) -> Path:

    if dataframe.empty:
        raise ValueError(
            "Não é posssível salvar um DataFrame VAZIO na camada gold"
        )
    else:
        CAMINHO_GOLD.mkdir(
            parents=True,
            exist_ok=True
        )

        caminho_arquivo = CAMINHO_GOLD / f"{nome_tabela}.parquet"
        dataframe.to_parquet(
            caminho_arquivo,
            index=False
        )

    return caminho_arquivo
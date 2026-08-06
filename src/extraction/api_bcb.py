""" Funções de extração de dados da API do BCB """

import pandas as pd
import requests

from src.config.indicadores_bcb import INDICADORES_BCB

BASE_URL_BCB = (
    "https://api.bcb.gov.br/dados/serie/"
    "bcdata.sgs.{codigo}/dados"
)

def buscar_serie_bcb (nome_indicador: str, data_inicial: str, data_final: str) -> pd.DataFrame:

    indicador = INDICADORES_BCB.get(nome_indicador)
    if indicador is None:
        raise ValueError(
            f"Indicador '{nome_indicador}' não encontrado"
        )
    codigo = indicador["codigo"]

    url = BASE_URL_BCB.format(codigo=codigo)

    parametros = {
        "formato": "json",
        "dataInicial": data_inicial,
        "dataFinal": data_final
    }
    
    resposta = requests.get(
        url,
        params=parametros,
        timeout=30
    )
    

    resposta.raise_for_status()
    dados = resposta.json()
    dataframe = pd.DataFrame(dados)

    return dataframe
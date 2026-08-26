""" Funções de extração de dados da API do BCB """


import pandas as pd
import requests

from src.config.indicadores_bcb import INDICADORES_BCB
from src.extraction.validar_datas import validar_periodo_bcb

class ErroApiBcb(RuntimeError):
    """Indica erro na API do bcb, no qual não poderá fornecer uma resposta válida conforme o caso"""

TEMPO_LIMITE_REQUISICAO = 30
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

    validar_periodo_bcb(data_inicial=data_inicial, data_final=data_final)

    url = BASE_URL_BCB.format(codigo=codigo)

    parametros = {
        "formato": "json",
        "dataInicial": data_inicial,
        "dataFinal": data_final
    }
    try:
        resposta = requests.get(
            url,
            params=parametros,
            timeout=TEMPO_LIMITE_REQUISICAO
        )

        resposta.raise_for_status()

    except requests.Timeout as erro:
        raise ErroApiBcb(
            f"A API do BCB excedeu  tempo limite ao consultar"
            f"'{nome_indicador}'"
        ) from erro
    except requests.HTTPError as erro:
        codigo_http = (
            erro.response.status_code
            if erro.response is not None
            else "desconhecido"
        )
        raise ErroApiBcb(
            f"A API do BCB retornou o erro HTTP {codigo_http} "
            f"ao consultar '{nome_indicador}'."
        ) from erro
    except requests.RequestException as erro:
        raise ErroApiBcb(
            f"Não foi possível conectar à API do BCB para consultar "
            f"'{nome_indicador}'."
        ) from erro

    try:
        dados = resposta.json()
    except requests.exceptions.JSONDecodeError as erro:
        raise ErroApiBcb(
            f"A API do BCB retornou um formato inesperado para "
            f"'{nome_indicador}'."
        ) from erro

    if not isinstance(dados, list):
        raise ErroApiBcb(
            f"A API do BCB retornou um formato inesperado para "
            f"'{nome_indicador}'."
        )
    dataframe = pd.DataFrame(dados)

    return dataframe
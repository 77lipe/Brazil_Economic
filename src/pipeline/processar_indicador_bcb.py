""" Orquestra o processamento de uma série econômica do BCB """

import pandas as pd

from src.extraction.api_bcb import buscar_serie_bcb
from src.storage.cmd_bronze import salvar_bronze
from src.validation.validar_dados_bcb import validar_dados_bcb
from src.transformation.transformar_dados_bcb import transformar_dados_bcb
from src.storage.cmd_silver import salvar_silver

def processor_indicador_bcb(
        nome_indicador: str,
        data_inicial: str,
        data_final: str
) -> pd.DataFrame:

    df_inicial = buscar_serie_bcb(
        nome_indicador=nome_indicador,
        data_inicial=data_inicial,
        data_final=data_final
    )

    salvar_bronze(dataframe=df_inicial, nome_indicador=nome_indicador)

    
    if validar_dados_bcb(df_inicial) is None:

        df_tratado = transformar_dados_bcb(
            dataframe=df_inicial,
            nome_indicador=nome_indicador
        )

        if df_tratado is not None: 
            salvar_silver(
                dataframe_tratado=df_tratado,
                nome_indicar=nome_indicador
            )

    return df_tratado
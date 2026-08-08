"""Teste manual da extração de dados do Banco Central."""

from src.extraction.api_bcb import buscar_serie_bcb
from src.validation.validar_dados_bcb import validar_dados_bcb
from src.transformation.transformar_dados_bcb import transformar_dados_bcb

## CAMADAS DE ARMAZENAMENTO (BRONZE - SILVER - GOLD) ##
from src.storage.cmd_bronze import salvar_bronze
from src.storage.cmd_silver import salvar_silver

# import pandas as pd

df_meta_selic = buscar_serie_bcb(
    nome_indicador="meta_selic",
    data_inicial="01/01/2025",
    data_final="31/12/2025",
)

caminho_bronze = salvar_bronze(
    dataframe=df_meta_selic,
    nome_indicador="meta_selic"
)

validar_dados_bcb(df_meta_selic)

df_meta_selic_tratado = transformar_dados_bcb(
    dataframe=df_meta_selic,
    nome_indicador="meta_selic",
)

caminho_silver = salvar_silver(
    dataframe_tratado=df_meta_selic_tratado,
    nome_indicar="meta_selic"
)


print("\nSELIC")
print(f"Arquivo Bronze - Selic\n{caminho_bronze}")

print(f'\n Dados Tratados\n{df_meta_selic_tratado.head()}')

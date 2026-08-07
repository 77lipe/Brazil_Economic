"""Teste manual da extração de dados do Banco Central."""

from src.extraction.api_bcb import buscar_serie_bcb
from src.validation.validar_dados_bcb import validar_dados_bcb
from src.transformation.transformar_dados_bcb import transformar_dados_bcb

df_meta_selic = buscar_serie_bcb(
    nome_indicador="meta_selic",
    data_inicial="01/01/2025",
    data_final="31/12/2025",
)

validar_dados_bcb(df_meta_selic)

df_meta_selic = transformar_dados_bcb(
    dataframe=df_meta_selic,
    nome_indicador="meta_selic",
)

print("\nSELIC")
print(df_meta_selic.head())
print()
print(df_meta_selic.tail())
print()
print(df_meta_selic.shape)
print()
print(df_meta_selic.dtypes)
print()

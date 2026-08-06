"""Teste manual da extração de dados do Banco Central."""

from src.extraction.api_bcb import buscar_serie_bcb


df_meta_selic = buscar_serie_bcb(
    nome_indicador="meta_selic",
    data_inicial="01/01/2025",
    data_final="31/12/2025",
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


df_dolar = buscar_serie_bcb(
    nome_indicador="dolar_venda",
    data_inicial="01/01/2025",
    data_final="31/01/2025",
)

print("\nDOLAR")
print(df_dolar.head())
print()
print(df_dolar.shape)